from fastapi import APIRouter, Depends, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from sqlalchemy.orm import Session

from ..config import get_settings
from ..database import get_db
from ..schemas import AuthResponse, LoginRequest, RegisterRequest
from ..services import login, register

router = APIRouter(prefix="/auth", tags=["auth"])
limiter = Limiter(key_func=get_remote_address)


@router.post("/register", response_model=AuthResponse)
@limiter.limit("5/minute")
def register_user(
    request: Request,
    payload: RegisterRequest,
    db: Session = Depends(get_db),
):
    settings = get_settings()
    return register(db, settings, payload)


@router.post("/login", response_model=AuthResponse)
@limiter.limit("10/minute")
def login_user(
    request: Request,
    payload: LoginRequest,
    db: Session = Depends(get_db),
):
    settings = get_settings()
    return login(db, settings, payload)
