from decimal import Decimal
from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..models import CartItem, Product


def add_to_cart(db: Session, user_id: str, product_id: str, quantity: int) -> CartItem:
    product = db.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product not found")
    if product.stock < quantity:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Insufficient stock")

    existing = (
        db.query(CartItem)
        .filter(CartItem.user_id == user_id, CartItem.product_id == product_id)
        .first()
    )

    if existing:
        existing.quantity += quantity
        db.commit()
        db.refresh(existing)
        return existing

    item = CartItem(user_id=user_id, product_id=product_id, quantity=quantity, price=product.price)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def get_cart(db: Session, user_id: str) -> List[CartItem]:
    return db.query(CartItem).filter(CartItem.user_id == user_id).all()


def remove_from_cart(db: Session, user_id: str, product_id: str) -> None:
    db.query(CartItem).filter(CartItem.user_id == user_id, CartItem.product_id == product_id).delete()
    db.commit()


def clear_cart(db: Session, user_id: str) -> None:
    db.query(CartItem).filter(CartItem.user_id == user_id).delete()
    db.commit()


def cart_total(db: Session, user_id: str) -> Decimal:
    items = db.query(CartItem).filter(CartItem.user_id == user_id).all()
    total = Decimal("0")
    for item in items:
        total += item.price * item.quantity
    return total
