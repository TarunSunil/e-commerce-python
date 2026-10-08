from datetime import datetime
from decimal import Decimal
from typing import List

from pydantic import BaseModel, Field


class ShippingAddress(BaseModel):
    address: str = Field(min_length=1, max_length=200)
    city: str = Field(min_length=1, max_length=100)
    state: str = Field(min_length=1, max_length=100)
    zipCode: str = Field(min_length=1, max_length=20)


class OrderCreate(BaseModel):
    shippingAddress: ShippingAddress


class OrderItemRead(BaseModel):
    productId: str = Field(alias="product_id")
    qty: int
    price: Decimal
    productName: str = Field(alias="product_name")
    unitPrice: Decimal = Field(alias="unit_price")

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
    shippingAddress: dict = Field(alias="shipping_address")

    class Config:
        from_attributes = True
        populate_by_name = True
        json_encoders = {
            Decimal: lambda v: float(v),
        }
