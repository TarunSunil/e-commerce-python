from sqlalchemy.orm import Session
from typing import List, Optional
from ..models.models import User, Product, Category, Order, OrderItem, CartItem
from ..schemas import schemas
from ..core.security import get_password_hash, verify_password


# User CRUD
def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()


def get_user_by_username(db: Session, username: str) -> Optional[User]:
    return db.query(User).filter(User.username == username).first()


def get_user(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, user: schemas.UserCreate) -> User:
    hashed_password = get_password_hash(user.password)
    db_user = User(
        email=user.email,
        username=user.username,
        full_name=user.full_name,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, username: str, password: str) -> Optional[User]:
    user = get_user_by_username(db, username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


# Category CRUD
def get_categories(db: Session, skip: int = 0, limit: int = 100) -> List[Category]:
    return db.query(Category).offset(skip).limit(limit).all()


def get_category(db: Session, category_id: int) -> Optional[Category]:
    return db.query(Category).filter(Category.id == category_id).first()


def create_category(db: Session, category: schemas.CategoryCreate) -> Category:
    db_category = Category(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def update_category(db: Session, category_id: int, category: schemas.CategoryUpdate) -> Optional[Category]:
    db_category = get_category(db, category_id)
    if not db_category:
        return None
    update_data = category.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_category, field, value)
    db.commit()
    db.refresh(db_category)
    return db_category


def delete_category(db: Session, category_id: int) -> bool:
    db_category = get_category(db, category_id)
    if not db_category:
        return False
    db.delete(db_category)
    db.commit()
    return True


# Product CRUD
def get_products(db: Session, skip: int = 0, limit: int = 100, category_id: Optional[int] = None) -> List[Product]:
    query = db.query(Product).filter(Product.is_active)
    if category_id:
        query = query.filter(Product.category_id == category_id)
    return query.offset(skip).limit(limit).all()


def get_product(db: Session, product_id: int) -> Optional[Product]:
    return db.query(Product).filter(Product.id == product_id).first()


def create_product(db: Session, product: schemas.ProductCreate) -> Product:
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, product_id: int, product: schemas.ProductUpdate) -> Optional[Product]:
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    update_data = product.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_product, field, value)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int) -> bool:
    db_product = get_product(db, product_id)
    if not db_product:
        return False
    db_product.is_active = False
    db.commit()
    return True


# Cart CRUD
def get_cart_items(db: Session, user_id: int) -> List[CartItem]:
    return db.query(CartItem).filter(CartItem.user_id == user_id).all()


def add_to_cart(db: Session, user_id: int, cart_item: schemas.CartItemCreate) -> CartItem:
    # Check if item already exists in cart
    existing_item = db.query(CartItem).filter(
        CartItem.user_id == user_id,
        CartItem.product_id == cart_item.product_id
    ).first()
    
    if existing_item:
        existing_item.quantity += cart_item.quantity
        db.commit()
        db.refresh(existing_item)
        return existing_item
    
    db_cart_item = CartItem(user_id=user_id, **cart_item.model_dump())
    db.add(db_cart_item)
    db.commit()
    db.refresh(db_cart_item)
    return db_cart_item


def update_cart_item(db: Session, cart_item_id: int, user_id: int, quantity: int) -> Optional[CartItem]:
    db_cart_item = db.query(CartItem).filter(
        CartItem.id == cart_item_id,
        CartItem.user_id == user_id
    ).first()
    if not db_cart_item:
        return None
    db_cart_item.quantity = quantity
    db.commit()
    db.refresh(db_cart_item)
    return db_cart_item


def remove_from_cart(db: Session, cart_item_id: int, user_id: int) -> bool:
    db_cart_item = db.query(CartItem).filter(
        CartItem.id == cart_item_id,
        CartItem.user_id == user_id
    ).first()
    if not db_cart_item:
        return False
    db.delete(db_cart_item)
    db.commit()
    return True


def clear_cart(db: Session, user_id: int) -> bool:
    db.query(CartItem).filter(CartItem.user_id == user_id).delete()
    db.commit()
    return True


# Order CRUD
def get_orders(db: Session, user_id: int, skip: int = 0, limit: int = 100) -> List[Order]:
    return db.query(Order).filter(Order.user_id == user_id).offset(skip).limit(limit).all()


def get_order(db: Session, order_id: int, user_id: int) -> Optional[Order]:
    return db.query(Order).filter(Order.id == order_id, Order.user_id == user_id).first()


def create_order(db: Session, user_id: int, order: schemas.OrderCreate) -> Optional[Order]:
    # Get cart items
    cart_items = get_cart_items(db, user_id)
    if not cart_items:
        return None
    
    # Calculate total
    total_amount = 0
    order_items = []
    
    for cart_item in cart_items:
        product = get_product(db, cart_item.product_id)
        if not product or product.stock < cart_item.quantity:
            return None
        
        item_total = product.price * cart_item.quantity
        total_amount += item_total
        
        order_items.append({
            "product_id": cart_item.product_id,
            "quantity": cart_item.quantity,
            "price": product.price
        })
        
        # Update stock
        product.stock -= cart_item.quantity
    
    # Create order
    db_order = Order(
        user_id=user_id,
        total_amount=total_amount,
        shipping_address=order.shipping_address
    )
    db.add(db_order)
    db.flush()
    
    # Create order items
    for item_data in order_items:
        db_order_item = OrderItem(order_id=db_order.id, **item_data)
        db.add(db_order_item)
    
    # Clear cart
    clear_cart(db, user_id)
    
    db.commit()
    db.refresh(db_order)
    return db_order


def get_all_orders(db: Session, skip: int = 0, limit: int = 100) -> List[Order]:
    return db.query(Order).offset(skip).limit(limit).all()


def update_order_status(db: Session, order_id: int, status: str) -> Optional[Order]:
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if not db_order:
        return None
    db_order.status = status
    db.commit()
    db.refresh(db_order)
    return db_order
