from __future__ import annotations

from decimal import Decimal
from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Index, Integer, Numeric, String
from sqlalchemy.orm import relationship

from ..database import Base


class CartItem(Base):
    __tablename__ = "carts"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    user_id = Column(String, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    product_id = Column(String, ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Numeric(12, 2), nullable=False)
    
    # Add relationship to Product for eager loading
    product = relationship("Product", lazy="joined")

    @property
    def product_name(self) -> str:
        return self.product.name

    @property
    def product_image(self) -> str | None:
        return self.product.images[0] if self.product.images else None

    @property
    def stock(self) -> int:
        return self.product.stock
    
    __table_args__ = (
        Index('ix_cart_user_product', 'user_id', 'product_id', unique=True),
    )
