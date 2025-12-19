from typing import List

from sqlalchemy.orm import Session

from ..models import Product, User


def recommend_by_product(db: Session, product_id: str, limit: int = 5) -> List[Product]:
    product = db.get(Product, product_id)
    if not product:
        return []

    target_categories = set(product.categories or [])
    all_products: List[Product] = db.query(Product).all()
    scored: List[tuple[Product, float]] = []

    for candidate in all_products:
        if candidate.id == product_id:
            continue
        categories = set(candidate.categories or [])
        if not target_categories and not categories:
            score = 0.0
        else:
            intersection = target_categories.intersection(categories)
            union = target_categories.union(categories)
            score = len(intersection) / len(union) if union else 0.0
        scored.append((candidate, score))

    scored.sort(key=lambda p: p[1], reverse=True)
    return [p for p, _ in scored[:limit]]


def recommend_by_user(db: Session, user_id: str, limit: int = 5) -> List[Product]:
    user = db.get(User, user_id)
    if not user:
        return []

    preferences = set(user.preferences or [])
    products: List[Product] = db.query(Product).all()

    if not preferences:
        return sorted(products, key=lambda p: p.stock or 0, reverse=True)[:limit]

    scored: List[tuple[Product, int]] = []
    for product in products:
        matches = sum(1 for cat in product.categories or [] if cat in preferences)
        scored.append((product, matches))

    scored.sort(key=lambda p: p[1], reverse=True)
    return [p for p, _ in scored[:limit]]
