from datetime import datetime, timezone
from uuid import UUID, uuid4

from sqlalchemy import Column, DateTime
from sqlmodel import Field, SQLModel 

from app.enums.enums import UserRoles, UserStatus


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


class User(SQLModel, table=True):
    id: UUID = Field(primary_key=True,default_factory=uuid4)

    school_id: UUID | None = Field( default=None, foreign_key="school.id", index=True  )

    name: str

    email: str

    password_hash: str | None = None

    role: UserRoles

    status: UserStatus = Field(
        default=UserStatus.INVITED
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