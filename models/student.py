from sqlmodel import SQLModel, Field, Relationship
from typing import List
from uuid import UUID, uuid4
from datetime import datetime, timezone
from models import User


class Student(SQLModel, table=True):
    user_id: UUID = Field(foreign_key='user.user_id')
    registration_number: str = Field(unique=True, index=True)
    gpa: float = Field(default=0.0)
    metadata: dict = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    user: User = Relationship(back_populates="student")
    enrollments: List["Enrollment"] = Relationship(back_populates="student")