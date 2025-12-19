from __future__ import annotations

from decimal import Decimal
from typing import List
from uuid import uuid4

from sqlalchemy import Column, Integer, Numeric, String
from sqlalchemy.dialects.postgresql import ARRAY, JSONB

from ..database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    name = Column(String, nullable=False, index=True)
    description = Column(String, nullable=True)
    categories = Column(ARRAY(String), nullable=False, default=list, index=True)
    price = Column(Numeric(12, 2), nullable=False)
    images = Column(ARRAY(String), nullable=False, default=list)
    stock = Column(Integer, nullable=False, default=0)
    attributes = Column(JSONB, nullable=False, default=dict)

