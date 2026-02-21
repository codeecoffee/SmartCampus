from enum import Enum
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship

from models.base import StandaloneModel

if TYPE_CHECKING:
    from .aiInteraction import AIInteraction
    from .chatSession import ChatSession
    from .notification import UserNotification
    from .professor import Professor
    from .student import Student

class UserRole(str, Enum):
    STUDENT = "student"
    PROFESSOR = "professor"
    ADMIN = "admin"

class UserStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"

class User(StandaloneModel, table=True):
    __tablename__ = "user"

    first_name: str
    last_name: str
    email: str = Field(unique=True, index=True)
    hashed_password: str
    role: UserRole = Field(default=UserRole.STUDENT, index=True)
    status: UserStatus = Field(default=UserStatus.ACTIVE, index=True)
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
    notifications: List["UserNotification"] = Relationship(back_populates="user")

