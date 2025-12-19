from __future__ import annotations

from decimal import Decimal
from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer, Numeric, String

from ..database import Base


class CartItem(Base):
    __tablename__ = "carts"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    user_id = Column(String, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    product_id = Column(String, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Numeric(12, 2), nullable=False)

