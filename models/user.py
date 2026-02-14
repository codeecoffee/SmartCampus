from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from uuid import UUID, uuid4
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    STUDENT = "student"
    PROFESSOR = "professor"
    ADMIN = "admin"

class UserStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"

class UserBase(SQLModel):
    first_name: str
    last_name: str
    email: str = Field(unique=True, index=True)
    hashed_password: str

class User(UserBase, table=True):
    user_id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True, index=True)
    role: UserRole = Field(default=UserRole.STUDENT, index=True)
    satus: UserStatus = Field(default=UserStatus.ACTIVE)

    student: Optional["Student"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={"uselist": False}
    )
    professor: Optional["Professor"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={"uselist": False}
    )
    chat_sessions: List["ChatSession"] = Relationship(back_populates="user")
    ai_interactions: List["AIInteraction"] = Relationship(back_populates="user")

