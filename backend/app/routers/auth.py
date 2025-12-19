from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..config import get_settings
from ..database import get_db
from ..schemas import AuthResponse, LoginRequest, RegisterRequest
from ..services import login, register

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=AuthResponse)
def register_user(request: RegisterRequest, db: Session = Depends(get_db)):
    settings = get_settings()
    return register(db, settings, request)


@router.post("/login", response_model=AuthResponse)
def login_user(request: LoginRequest, db: Session = Depends(get_db)):
    settings = get_settings()
    return login(db, settings, request)
