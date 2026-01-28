from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..dependencies import CurrentUser, require_admin
from ..models import Product
from ..schemas import ProductCreate, ProductRead, ProductUpdate
from ..services import create_product, delete_product, get_product, get_products, update_product

router = APIRouter(prefix="/products", tags=["products"])


@router.get("", response_model=list[ProductRead])
def list_products(
    page: int = 0,
    size: int = 100,
    category: str | None = None,
    q: str | None = None,
    db: Session = Depends(get_db),
):
    return get_products(db, page, size, category, q)


@router.get("/{product_id}", response_model=ProductRead)
def get_product_by_id(product_id: str, db: Session = Depends(get_db)):
    product = get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product


@router.post("", response_model=ProductRead)
def create_product_route(
    payload: ProductCreate,
    db: Session = Depends(get_db),
    _: CurrentUser = Depends(require_admin),
):
    product = Product(**payload.dict())
    return create_product(db, product)


@router.put("/{product_id}", response_model=ProductRead)
def update_product_route(
    product_id: str,
    payload: ProductUpdate,
    db: Session = Depends(get_db),
    _: CurrentUser = Depends(require_admin),
):
    updates = Product(**payload.dict())
    try:
        return update_product(db, product_id, updates)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")


@router.delete("/{product_id}")
def delete_product_route(
    product_id: str,
    db: Session = Depends(get_db),
    _: CurrentUser = Depends(require_admin),
):
    try:
        delete_product(db, product_id)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return {"status": "deleted"}
