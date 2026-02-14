from datetime import datetime,timezone
from sqlmodel import Field, SQLModel, Field, Relationship
from uuid import UUID
from typing import List

from models import User

class Professor(SQLModel, table=True):
    user_id: UUID = Field(foreign_key="user.user_id", primary_key=True)
    department: str =Field(index=True)
    office_hours: str

    created_at: datetime = Field(default_factory= lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory= lambda: datetime.now(timezone.utc))

    user: User = Relationship(back_populates="professor")
    courses: List["Course"] = Relationship(back_populates="professor")
