from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..config import Settings
from ..models import User
from ..schemas import AuthResponse, LoginRequest, RegisterRequest
from ..security import create_access_token, hash_password, verify_password


def register(db: Session, settings: Settings, request: RegisterRequest) -> AuthResponse:
    existing = db.query(User).filter(User.email == request.email).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")

    user = User(
        name=request.name,
        email=request.email,
        password_hash=hash_password(request.password),
        roles=["USER"],
        preferences=[],
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    token = create_access_token(email=user.email, user_id=user.id, roles=user.roles, settings=settings)
    return AuthResponse(token=token, userId=user.id, email=user.email, name=user.name, roles=user.roles)


def login(db: Session, settings: Settings, request: LoginRequest) -> AuthResponse:
    user = db.query(User).filter(User.email == request.email).first()
    if not user or not verify_password(request.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email or password")

    token = create_access_token(email=user.email, user_id=user.id, roles=user.roles, settings=settings)
    return AuthResponse(token=token, userId=user.id, email=user.email, name=user.name, roles=user.roles)
