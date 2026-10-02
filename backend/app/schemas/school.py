from pydantic import BaseModel, ConfigDict, EmailStr, Field
from app.enums.enums import SchoolStatus
from uuid import UUID
from datetime import datetime

class SchoolCreate(BaseModel):

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    name: str = Field(
        min_length=3,
        max_length=150,
    )

    address: str | None = Field(
        default=None,
        min_length=5,
        max_length=300,
    )

    phone: str | None = Field(
        default=None,
        min_length=7,
        max_length=20,
    )

    email: EmailStr | None = None

    logo_url: str | None = None

    timezone: str = Field(
        default="UTC",
        min_length=1,
        max_length=100,
    )
    
class SchoolRead(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: UUID
    name: str
    address: str | None
    phone: str | None
    email: EmailStr | None
    logo_url: str | None
    timezone: str
    status: SchoolStatus
    created_at: datetime
    updated_at: datetime