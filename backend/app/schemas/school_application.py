from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.enums.enums import SchoolApplicationStatus


class SchoolApplicationCreate(BaseModel):

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    school_name: str = Field(
        min_length=3,
        max_length=150,
    )

    contact_name: str = Field(
        min_length=3,
        max_length=100,
    )

    contact_email: EmailStr

    contact_phone: str | None = Field(
        default=None,
        min_length=7,
        max_length=20,
    )

    expected_students: int | None = Field(
        default=None,
        ge=1,
        le=100000,
    )


class SchoolApplicationRead(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: UUID
    school_name: str
    contact_name: str
    contact_email: EmailStr
    contact_phone: str | None
    expected_students: int | None
    status: SchoolApplicationStatus
    reviewed_by: UUID | None
    reviewed_at: datetime | None
    created_at: datetime