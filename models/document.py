from typing import Optional, List, TYPE_CHECKING
from uuid import UUID
from sqlmodel import Field, Relationship
from enum import Enum
from models.base import StandaloneModel

if TYPE_CHECKING:
    from .documentInteraction import DocumentInteraction

class DocumentType(str, Enum):
    SYLLABUS = "syllabus"
    REGULATION = "regulation"
    GUIDELINE = "guideline"
    RESEARCH = "research"

class Document(StandaloneModel, table=True):
    __tablename__ = "document"
    title: str = Field(index=True)
    doc_type: DocumentType = Field(index=True)
    content: str
    #Vector search
    embedding: Optional[List[float]] = Field(default=None)
    #Source tracking
    file_url: Optional[str]= Field()
    uploaded_by: Optional[UUID] = Field(foreign_key="user.id")
    doc_interactions: List["DocInteraction"] = Relationship(back_populates="document")