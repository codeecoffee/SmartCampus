from typing import TYPE_CHECKING, Any, Dict, List, Optional
from uuid import UUID
from sqlmodel import Field, Relationship, Column
from sqlalchemy import JSON
from models.base import StandaloneModel
from datetime import datetime, timezone

if TYPE_CHECKING:
    from .chatSession import ChatSession
    from .documentInteraction import DocumentInteraction
    from .user import User

class AIInteraction(StandaloneModel, table=True):
    __tablename__ = "ai_interaction"
    user_id: UUID = Field(foreign_key="user.id", index=True)
    session_id: UUID = Field(foreign_key="chat_session.id", index=True)
    action_executed: bool = Field(default=False)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), index=True)

    interaction_metadata: Optional[Dict[str, Any]] = Field(
        default=None, sa_column=Column("interaction_metadata", JSON, nullable=True)
    )

    user: "User" = Relationship(back_populates="interactions")
    session: "ChatSession" = Relationship(back_populates="interactions")
    documents_used: List["DocumentInteraction"] = Relationship(back_populates="interaction")
