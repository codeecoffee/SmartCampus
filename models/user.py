from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from uuid import UUID, uuid4
from enum import Enum

class UserBase(SQLModel):
    first_name: str
    last_name: str
    email: str = Field(unique=True, index=True)
    hashed_password: str

class User(UserBase, table=True):
    user_id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True, index=True)
    role: Enum
    satus: Enum
    student: Optional["Student"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={"uselist": False}
    )


class UserRole(str, Enum):
    STUDENT = "student"
    PROFESSOR = "professor"
    ADMIN = "admin"

class UserStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"