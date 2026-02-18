from datetime import datetime,timezone
from sqlmodel import Field, SQLModel, Field, Relationship
from uuid import UUID
from typing import List

from models import User
from models.base import TimestampOnlyModel


class Professor(TimestampOnlyModel, table=True):
    user_id: UUID = Field(foreign_key="user.user_id", primary_key=True, ondelete="CASCADE")
    department: str = Field(index=True)
    office_hours: str

    user: User = Relationship(back_populates="professor")
    courses: List["Course"] = Relationship(back_populates="professor")
