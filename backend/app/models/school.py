from datetime import datetime, timezone
from uuid import UUID, uuid4
from sqlalchemy import Column, DateTime
from sqlmodel import Field, SQLModel
from app.enums.enums import SchoolStatus

def _utc_now() -> datetime:
    return datetime.now(timezone.utc)

class School(SQLModel, table=True):
    id: UUID = Field(  default_factory=uuid4, primary_key=True )
    name: str
    address: str | None = None
    phone: str | None = None
    email: str | None = None
    logo_url: str | None = None
    timezone: str = Field(default="UTC")
    status: SchoolStatus = Field(
        default=SchoolStatus.ACTIVE
    )
    created_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            nullable=False,
            default=_utc_now
        )
    )
    updated_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            nullable=False,
            default=_utc_now,
            onupdate=_utc_now
        )
    )