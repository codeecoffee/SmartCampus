from sqlmodel import SQLModel, Field, Relationship, Column, JSON
from typing import List, Optional
from uuid import UUID, uuid4
from models import User
from models.base import TimestampOnlyModel


class Student(TimestampOnlyModel, table=True):
    user_id: UUID = Field(foreign_key='user.user_id', primary_key=True, ondelete="CASCADE")
    registration_number: str = Field(unique=True, index=True)
    gpa: Optional[float] = Field(default=0.0)
    metadata: Optional[dict] = Field(default=None, sa_column=Column(JSON))
    user: User = Relationship(back_populates="student")
    enrollments: List["Enrollment"] = Relationship(back_populates="student")