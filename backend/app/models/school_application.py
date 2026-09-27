from datetime import datetime, timezone
from typing import TYPE_CHECKING, Optional
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy import DateTime, Column

from app.enums.enums import SchoolApplicationStatus

if TYPE_CHECKING:
    from app.models.user import User


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


class SchoolApplication(SQLModel, table=True):
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True
    )

    school_name: str
    contact_name: str
    contact_email: str
    contact_phone: Optional[str] = None
    expected_students: Optional[int] = None

    status: SchoolApplicationStatus = Field(
        default=SchoolApplicationStatus.PENDING
    )

    reviewed_by: Optional[UUID] = Field(
        default=None,
        foreign_key="user.id"
    )

    reviewed_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), nullable=True)
    )

    created_at: datetime = Field(
        default_factory=_utc_now,
        sa_column=Column(DateTime(timezone=True), nullable=False)
    )

   
    reviewer: Optional["User"] = Relationship(
        sa_relationship_kwargs={"foreign_keys": "[SchoolApplication.reviewed_by]"}
    )