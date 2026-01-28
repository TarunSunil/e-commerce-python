from decimal import Decimal
from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session, joinedload

from ..models import CartItem, Order, OrderItem, Product, User


def create_order(db: Session, user_id: str) -> Order:
    # Use joinedload to avoid N+1 query problem
    cart_items: List[CartItem] = (
        db.query(CartItem)
        .options(joinedload(CartItem.product))
        .filter(CartItem.user_id == user_id)
        .all()
    )
    if not cart_items:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cart is empty")

    order_items: List[OrderItem] = []
    total = Decimal("0")
    
    try:
        # Start transaction (implicit with Session, but made explicit for clarity)
        for item in cart_items:
            # Access product through relationship (already loaded via joinedload)
            product = item.product if hasattr(item, 'product') else db.get(Product, item.product_id)
            if not product:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Product not found: {item.product_id}")
            if product.stock < item.quantity:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Insufficient stock for product: {product.name}")

            product.stock -= item.quantity
            db.add(product)

            order_item = OrderItem(product_id=item.product_id, qty=item.quantity, price=item.price)
            order_items.append(order_item)
            total += item.price * item.quantity

        order = Order(user_id=user_id, items=order_items, total=total)
        db.add(order)

        # Clear cart after order creation
        db.query(CartItem).filter(CartItem.user_id == user_id).delete()

        # Append to user's order ids if needed
        user = db.get(User, user_id)
        if user and hasattr(user, "order_ids"):
            # Attribute kept for parity; may not exist
            existing = getattr(user, "order_ids") or []
            existing.append(order.id)
            setattr(user, "order_ids", existing)
            db.add(user)

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
