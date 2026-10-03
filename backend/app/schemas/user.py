from pydantic import BaseModel, ConfigDict, EmailStr, Field
from datetime import datetime
from uuid import UUID

from app.enums.enums import UserRoles, UserStatus


class UserInviteCreate(BaseModel):

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    name: str = Field(
        min_length=3,
        max_length=100,
    )

    email: EmailStr

    role: UserRoles


class UserRead(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: UUID
    school_id: UUID | None
    name: str
    email: EmailStr
    role: UserRoles
    status: UserStatus
    created_at: datetime
    updated_at: datetime