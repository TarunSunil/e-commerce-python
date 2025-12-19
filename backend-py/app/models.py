from __future__ import annotations

from typing import List, Optional, Dict
from datetime import datetime
from decimal import Decimal

from beanie import Document
from pydantic import BaseModel, Field
from pymongo import IndexModel


class Product(Document):
    id: Optional[str] = Field(default=None)  # keep string ids for compatibility
    name: str
    description: Optional[str] = None
    categories: List[str] = Field(default_factory=list)
    price: Decimal
    images: List[str] = Field(default_factory=list)
    stock: int
    attributes: Dict[str, str] = Field(default_factory=dict)

    class Settings:
        name = "products"
        indexes = [
            IndexModel([("name", 1)]),
            IndexModel([("categories", 1)]),
        ]


class User(Document):
    id: Optional[str] = Field(default=None)
    name: Optional[str] = None
    email: str
    passwordHash: str
    roles: List[str] = Field(default_factory=list)
    preferences: List[str] = Field(default_factory=list)
    orderIds: List[str] = Field(default_factory=list)
    createdAt: datetime

    class Settings:
        name = "users"
        indexes = [
            IndexModel([("email", 1)], unique=True),
        ]


class CartItem(Document):
    id: Optional[str] = Field(default=None)
    userId: str
    productId: str
    quantity: int
    price: Decimal

    class Settings:
        name = "carts"
        indexes = [
            IndexModel([("userId", 1)]),
        ]


class OrderItem(BaseModel):
    productId: str
    qty: int
    price: Decimal


class Order(Document):
    id: Optional[str] = Field(default=None)
    userId: str
    items: List[OrderItem] = Field(default_factory=list)
    status: str = Field(default="placed")
    total: Decimal
    createdAt: datetime

    class Settings:
        name = "orders"
        indexes = [
            IndexModel([("userId", 1)]),
        ]
