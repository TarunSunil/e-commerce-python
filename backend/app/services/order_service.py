from decimal import Decimal
from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session, joinedload

from ..models import CartItem, Order, OrderItem, Product
from ..schemas.order import ShippingAddress


def create_order(db: Session, user_id: str, shipping_address: ShippingAddress) -> Order:
    cart_items: List[CartItem] = (
        db.query(CartItem)
        .filter(CartItem.user_id == user_id)
        .all()
    )
    if not cart_items:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cart is empty")

    order_items: List[OrderItem] = []
    total = Decimal("0")
    
    try:
        product_ids = sorted({item.product_id for item in cart_items})
        locked_products = (
            db.query(Product)
            .filter(Product.id.in_(product_ids))
            .order_by(Product.id)
            .with_for_update()
            .all()
        )
        products = {product.id: product for product in locked_products}
        changed_lines = []
        for item in cart_items:
            product = products.get(item.product_id)
            if not product:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Product not found: {item.product_id}")
            if item.price != product.price:
                changed_lines.append({
                    "productId": product.id,
                    "name": product.name,
                    "oldPrice": float(item.price),
                    "newPrice": float(product.price),
                })
        if changed_lines:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail={"message": "Prices changed", "changedLines": changed_lines},
            )

        for item in cart_items:
            product = products[item.product_id]
            if product.stock < item.quantity:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Insufficient stock for product: {product.name}")

            product.stock -= item.quantity
            db.add(product)

            order_item = OrderItem(
                product_id=item.product_id,
                qty=item.quantity,
                price=item.price,
                product_name=product.name,
                unit_price=product.price,
            )
            order_items.append(order_item)
            total += item.price * item.quantity

        order = Order(
            user_id=user_id,
            items=order_items,
            total=total,
            shipping_address=shipping_address.model_dump(by_alias=True),
        )
        db.add(order)

        # Clear cart after order creation
        db.query(CartItem).filter(CartItem.user_id == user_id).delete()

        db.commit()
        db.refresh(order)
        return order
    except HTTPException:
        db.rollback()
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to create order: {str(e)}")


def get_user_orders(db: Session, user_id: str) -> List[Order]:
    return (
        db.query(Order)
        .filter(Order.user_id == user_id)
        .order_by(Order.created_at.desc())
        .all()
    )


def get_order(db: Session, order_id: str) -> Order:
    order = db.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return order
