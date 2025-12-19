from typing import List

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from .config import get_settings
from .database import get_db
from .models import User
from .security import decode_token


bearer_scheme = HTTPBearer(auto_error=True)


class CurrentUser:
    def __init__(self, id: str, email: str, roles: List[str]):
        self.id = id
        self.email = email
        self.roles = roles or []

    def is_admin(self) -> bool:
        return "ADMIN" in self.roles


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db),
):
    settings = get_settings()
    token = credentials.credentials
    payload = decode_token(token, settings)

    user_id: str | None = payload.get("userId")
    email: str | None = payload.get("sub")
    roles: List[str] = payload.get("roles") or []

    if not user_id or not email:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload")

    user: User | None = db.get(User, user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    return CurrentUser(user.id, user.email, roles)


def require_admin(current_user: CurrentUser = Depends(get_current_user)):
    if not current_user.is_admin():
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin role required")
    return current_user
