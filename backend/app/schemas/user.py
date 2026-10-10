from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserRead(BaseModel):
    id: str
    name: Optional[str]
    email: EmailStr
    roles: List[str]
    preferences: List[str]
    createdAt: datetime = Field(validation_alias="created_at", serialization_alias="createdAt")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )
