from decimal import Decimal
from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    categories: List[str] = Field(default_factory=list)
    price: Decimal
    images: List[str] = Field(default_factory=list)
    stock: int
    attributes: Dict[str, str] = Field(default_factory=dict)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductRead(ProductBase):
    id: str

    class Config:
        from_attributes = True
        json_encoders = {
            Decimal: lambda v: float(v),
        }
