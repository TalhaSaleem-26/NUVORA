
from datetime import datetime, timezone
from uuid import uuid4
from sqlmodel import SQLModel, Field
from app.enums.enums import SchoolStatus

def _uuid() -> str:
    return str(uuid4())

def _utc_now() -> datetime:
    return datetime.now(timezone.utc)




class School(SQLModel, table=True):
    id: str = Field(default_factory=_uuid, primary_key=True)
    name: str
    address: str | None = None
    phone: str | None = None
    email: str | None = None
    logo_url: str | None = None
    timezone: str = Field(default="UTC")  
    status: SchoolStatus = Field(default=SchoolStatus.ACTIVE)
    subscription: bool = Field(default=False)
    
  
    created_at: datetime = Field(default_factory=_utc_now)
    updated_at: datetime = Field(
        default_factory=_utc_now, 
        sa_column_kwargs={"onupdate": _utc_now}
    )