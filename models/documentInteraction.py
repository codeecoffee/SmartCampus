from sqlalchemy.ext.baked import bakery
from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID, uuid4
from typing import Optional, List, TYPE_CHECKING
from datetime import timezone, datetime
from .aiInteraction import AIInteraction
from .document import Document

if TYPE_CHECKING:
    from .aiInteraction import AIInteraction
    from .document import Document

class DocumentInteraction(SQLModel,table=True):
    doc_interaction_id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    interaction_id: UUID = Field(foreign_key="ai_interaction.id")
    doc_id: UUID = Field(foreign_key="document.id", index=True)
    relevance_score: float
    usage_order: int
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    #Relationships
    interaction:AIInteraction = Relationship(back_populates="documents_used")
    document: Document = Relationship(back_populates="document_interactions")