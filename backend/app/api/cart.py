from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..core.database import get_db
from ..schemas import schemas
from ..crud import crud
from .auth import get_current_active_user

router = APIRouter()


@router.get("/", response_model=schemas.Cart)
def get_cart(
    current_user: schemas.User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    cart_items = crud.get_cart_items(db, user_id=current_user.id)
    total = sum(item.product.price * item.quantity for item in cart_items)
    return {"items": cart_items, "total": total}


@router.post("/items", response_model=schemas.CartItem)
def add_to_cart(
    cart_item: schemas.CartItemCreate,
    current_user: schemas.User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    # Verify product exists
    product = crud.get_product(db, cart_item.product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if product.stock < cart_item.quantity:
        raise HTTPException(status_code=400, detail="Not enough stock available")
    
    return crud.add_to_cart(db=db, user_id=current_user.id, cart_item=cart_item)


@router.put("/items/{cart_item_id}", response_model=schemas.CartItem)
def update_cart_item(
    cart_item_id: int,
    cart_item: schemas.CartItemUpdate,
    current_user: schemas.User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    db_cart_item = crud.update_cart_item(
        db, cart_item_id=cart_item_id, user_id=current_user.id, quantity=cart_item.quantity
    )
    if db_cart_item is None:
        raise HTTPException(status_code=404, detail="Cart item not found")
    return db_cart_item


@router.delete("/items/{cart_item_id}")
def remove_from_cart(
    cart_item_id: int,
    current_user: schemas.User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    success = crud.remove_from_cart(db, cart_item_id=cart_item_id, user_id=current_user.id)
    if not success:
        raise HTTPException(status_code=404, detail="Cart item not found")
    return {"message": "Item removed from cart"}


@router.delete("/")
def clear_cart(
    current_user: schemas.User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    crud.clear_cart(db, user_id=current_user.id)
    return {"message": "Cart cleared"}
