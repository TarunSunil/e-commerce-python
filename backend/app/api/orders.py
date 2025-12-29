from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..core.database import get_db
from ..schemas import schemas
from ..crud import crud
from .auth import get_current_active_user, get_admin_user

router = APIRouter()


@router.get("/", response_model=List[schemas.Order])
def get_orders(
    skip: int = 0,
    limit: int = 100,
    current_user: schemas.User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    orders = crud.get_orders(db, user_id=current_user.id, skip=skip, limit=limit)
    return orders


@router.get("/{order_id}", response_model=schemas.Order)
def get_order(
    order_id: int,
    current_user: schemas.User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    db_order = crud.get_order(db, order_id=order_id, user_id=current_user.id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order


@router.post("/", response_model=schemas.Order)
def create_order(
    order: schemas.OrderCreate,
    current_user: schemas.User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    db_order = crud.create_order(db=db, user_id=current_user.id, order=order)
    if db_order is None:
        raise HTTPException(status_code=400, detail="Cannot create order. Check cart and product stock.")
    return db_order


@router.get("/admin/all", response_model=List[schemas.Order])
def get_all_orders(
    skip: int = 0,
    limit: int = 100,
    current_user: schemas.User = Depends(get_admin_user),
    db: Session = Depends(get_db)
):
    orders = crud.get_all_orders(db, skip=skip, limit=limit)
    return orders


@router.put("/{order_id}/status", response_model=schemas.Order)
def update_order_status(
    order_id: int,
    status: str,
    current_user: schemas.User = Depends(get_admin_user),
    db: Session = Depends(get_db)
):
    valid_statuses = ["pending", "processing", "shipped", "delivered", "cancelled"]
    if status not in valid_statuses:
        raise HTTPException(status_code=400, detail=f"Invalid status. Must be one of: {valid_statuses}")
    
    db_order = crud.update_order_status(db, order_id=order_id, status=status)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order
