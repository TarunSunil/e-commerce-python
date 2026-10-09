from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class CartItemCreate(BaseModel):
    productId: str
    quantity: int = Field(gt=0)


class CartItemRead(BaseModel):
    id: str
    userId: str = Field(validation_alias="user_id", serialization_alias="userId")
    productId: str = Field(validation_alias="product_id", serialization_alias="productId")
    quantity: int
    price: Decimal
    productName: str = Field(validation_alias="product_name", serialization_alias="productName")
    productImage: str | None = Field(
        default=None,
        validation_alias="product_image",
        serialization_alias="productImage",
    )
    stock: int

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        json_encoders={Decimal: lambda v: float(v)},
    )
