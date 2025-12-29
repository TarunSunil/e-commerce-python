from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime


# User Schemas
class UserBase(BaseModel):
    email: EmailStr
    username: str
    full_name: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class User(UserBase):
    id: int
    is_active: bool
    is_admin: bool
    created_at: datetime
    
    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


# Category Schemas
class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class Category(CategoryBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True


# Product Schemas
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
    image_url: Optional[str] = None
    category_id: Optional[int] = None


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)
    image_url: Optional[str] = None
    category_id: Optional[int] = None
    is_active: Optional[bool] = None


class Product(ProductBase):
    id: int
    is_active: bool
    created_at: datetime
    category: Optional[Category] = None
    
    class Config:
        from_attributes = True


# Cart Schemas
class CartItemBase(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)


class CartItemCreate(CartItemBase):
    pass


class CartItemUpdate(BaseModel):
    quantity: int = Field(gt=0)


class CartItem(CartItemBase):
    id: int
    user_id: int
    created_at: datetime
    product: Product
    
    class Config:
        from_attributes = True


class Cart(BaseModel):
    items: List[CartItem]
    total: float


# Order Schemas
class OrderItemBase(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)
    price: float


class OrderItem(OrderItemBase):
    id: int
    order_id: int
    product: Optional[Product] = None
    
    class Config:
        from_attributes = True


class OrderBase(BaseModel):
    shipping_address: str


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    user_id: int
    total_amount: float
    status: str
    created_at: datetime
    order_items: List[OrderItem]
    
    class Config:
        from_attributes = True
