from datetime import datetime
from decimal import Decimal
from typing import List

from pydantic import BaseModel, ConfigDict, Field


class ShippingAddress(BaseModel):
    address: str = Field(min_length=1, max_length=200)
    city: str = Field(min_length=1, max_length=100)
    state: str = Field(min_length=1, max_length=100)
    zipCode: str = Field(min_length=1, max_length=20)


class OrderCreate(BaseModel):
    shippingAddress: ShippingAddress


class OrderItemRead(BaseModel):
    productId: str = Field(validation_alias="product_id", serialization_alias="productId")
    qty: int
    price: Decimal
    productName: str = Field(validation_alias="product_name", serialization_alias="productName")
    unitPrice: Decimal = Field(validation_alias="unit_price", serialization_alias="unitPrice")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        json_encoders={Decimal: lambda v: float(v)},
    )


class OrderRead(BaseModel):
    id: str
    userId: str = Field(validation_alias="user_id", serialization_alias="userId")
    items: List[OrderItemRead]
    status: str
    total: Decimal
    createdAt: datetime = Field(validation_alias="created_at", serialization_alias="createdAt")
    shippingAddress: dict = Field(
        validation_alias="shipping_address",
        serialization_alias="shippingAddress",
    )

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        json_encoders={Decimal: lambda v: float(v)},
    )
