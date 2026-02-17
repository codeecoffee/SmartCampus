from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from typing import Optional
from datetime import datetime, timezone

class AIInteraction(SQLModel, table=True):
    interaction_id: Optional[UUID] = Field(default_factory =uuid4,primary_key=True)

    message: str
    bot_response: str
    action_executed: Optional[str] = None
    context: dict = Field(default_factory=dict)
