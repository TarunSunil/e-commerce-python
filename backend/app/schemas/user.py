from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr


class UserRead(BaseModel):
    id: str
    name: Optional[str]
    email: EmailStr
    roles: List[str]
    preferences: List[str]
    created_at: datetime

    class Config:
        from_attributes = True
