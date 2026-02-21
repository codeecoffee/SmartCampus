from datetime import datetime,timezone
from typing import List, TYPE_CHECKING
from uuid import UUID
from sqlmodel import Field, SQLModel, Field, Relationship
from models import User
from models.base import TimestampOnlyModel

if TYPE_CHECKING:
    from .course import Course
    from .user import User

class Professor(TimestampOnlyModel, table=True):
    __tablename__ = "professor"
    user_id: UUID = Field(foreign_key="user.id", primary_key=True, ondelete="CASCADE")
    department: str = Field(index=True)
    office_hours: str

    user: "User" = Relationship(back_populates="professor")
    courses: List["Course"] = Relationship(back_populates="professor")
