from datetime import datetime, timezone
from typing import TYPE_CHECKING, Any, List, Optional, Dict
from uuid import UUID
from sqlmodel import Field, Relationship, Column, JSON
from models.base import StandaloneModel

if TYPE_CHECKING:
    from .aiInteraction import AIInteraction
    from .user import User
class ChatSession(StandaloneModel, table=True):
    __tablename__ = "chat_session"
    user_id: UUID = Field(foreign_key="user.id", index=True)
    title: Optional[str] = Field(default=None)
    # context_widow: Optional[Dict[str, Any]] = Field(default=None)
    context_widow: Optional[Dict[str, Any]] = Field(
        default=None,
       sa_column=Column("context_widow", JSON, nullable=True),
    )

    is_active: bool = Field(default=True, index=True)
    ended_at: Optional[datetime] = Field(default=None)
    user: "User" = Relationship(back_populates="chat_sessions")
    interactions: List["AIInteraction"] = Relationship(back_populates="session")