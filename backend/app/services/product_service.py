from typing import List, Optional

from sqlalchemy import or_
from sqlalchemy.orm import Session

from ..models import Product


def get_products(db: Session, page: int, size: int, category: Optional[str], search: Optional[str]) -> List[Product]:
    query = db.query(Product)

    if search:
        pattern = f"%{search}%"
        query = query.filter(or_(Product.name.ilike(pattern), Product.description.ilike(pattern)))

    if category:
        query = query.filter(Product.categories.any(category))

    return query.offset(page * size).limit(size).all()


def get_product(db: Session, product_id: str) -> Optional[Product]:
    return db.get(Product, product_id)


def create_product(db: Session, product: Product) -> Product:
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def update_product(db: Session, product_id: str, updates: Product) -> Product:
    existing = db.get(Product, product_id)
    if not existing:
        raise ValueError("Product not found")

    existing.name = updates.name
    existing.description = updates.description
    existing.categories = updates.categories
    existing.price = updates.price
    existing.images = updates.images
    existing.stock = updates.stock
    existing.attributes = updates.attributes

    db.commit()
    db.refresh(existing)
    return existing


def delete_product(db: Session, product_id: str) -> None:
    existing = db.get(Product, product_id)
    if not existing:
        raise ValueError("Product not found")
    db.delete(existing)
    db.commit()
