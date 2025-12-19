import httpx
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..config import get_settings
from ..database import get_db
from ..dependencies import CurrentUser, get_current_user
from ..schemas import ProductRead
from ..services import recommend_by_product, recommend_by_user

router = APIRouter(prefix="/recommend", tags=["recommendations"])


def _recommender_base() -> str:
    return get_settings().recommender_url.rstrip("/")


async def _proxy_recommender(path: str, limit: int):
    base = _recommender_base()
    url = f"{base}{path}"
    timeout = httpx.Timeout(connect=0.5, read=2.0)
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            resp = await client.get(url, params={"limit": str(limit)})
            if resp.status_code == 200:
                data = resp.json()
                if isinstance(data, dict) and "items" in data:
                    return data.get("items")
                if isinstance(data, list):
                    return data
    except httpx.RequestError:
        return None
    return None


@router.get("/{product_id}", response_model=list[ProductRead])
async def recommend_for_product(product_id: str, limit: int = 5, db: Session = Depends(get_db)):
    proxied = await _proxy_recommender(f"/recommend/{product_id}", limit)
    if proxied is not None:
        return proxied
    return recommend_by_product(db, product_id, limit)


@router.get("/user/{user_id}", response_model=list[ProductRead])
async def recommend_for_user(
    user_id: str,
    limit: int = 5,
    db: Session = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user),
):
    if current_user.id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")

    proxied = await _proxy_recommender(f"/recommend/user/{user_id}", limit)
    if proxied is not None:
        return proxied
    return recommend_by_user(db, user_id, limit)
