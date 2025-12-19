from datetime import datetime
from decimal import Decimal
from typing import List

from pydantic import BaseModel, Field


class OrderItemRead(BaseModel):
    productId: str = Field(alias="product_id")
    qty: int
    price: Decimal

    class Config:
        from_attributes = True
        populate_by_name = True
        json_encoders = {
            Decimal: lambda v: float(v),
        }


class OrderRead(BaseModel):
    id: str
    userId: str = Field(alias="user_id")
    items: List[OrderItemRead]
    status: str
    total: Decimal
    createdAt: datetime = Field(alias="created_at")

    class Config:
        from_attributes = True
        populate_by_name = True
        json_encoders = {
            Decimal: lambda v: float(v),
        }
