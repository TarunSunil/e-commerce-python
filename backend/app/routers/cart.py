from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..dependencies import CurrentUser, get_current_user
from ..schemas import CartItemCreate, CartItemRead
from ..services import add_to_cart, cart_total, clear_cart, get_cart, remove_from_cart

router = APIRouter(prefix="/cart", tags=["cart"])


@router.post("", response_model=CartItemRead)
def add_item(
    payload: CartItemCreate,
    db: Session = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    return add_to_cart(db, current_user.id, payload.productId, payload.quantity)


@router.get("", response_model=list[CartItemRead])
def get_user_cart(
    db: Session = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    return get_cart(db, current_user.id)


@router.get("/total")
def get_cart_total(
    db: Session = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    total = cart_total(db, current_user.id)
    return {"total": float(total)}


@router.delete("/{product_id}")
def delete_item(
    product_id: str,
    db: Session = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    remove_from_cart(db, current_user.id, product_id)
    return {"status": "removed"}


@router.delete("")
def clear_user_cart(
    db: Session = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    clear_cart(db, current_user.id)
    return {"status": "cleared"}
