from decimal import Decimal

from pydantic import BaseModel, Field


class CartItemCreate(BaseModel):
    productId: str
    quantity: int = Field(gt=0)


class CartItemRead(BaseModel):
    id: str
    userId: str = Field(alias="user_id")
    productId: str = Field(alias="product_id")
    quantity: int
    price: Decimal
    productName: str = Field(alias="product_name")
    productImage: str | None = Field(default=None, alias="product_image")
    stock: int

    class Config:
        from_attributes = True
        populate_by_name = True
        json_encoders = {
            Decimal: lambda v: float(v),
        }
