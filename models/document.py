from typing import Optional, List, TYPE_CHECKING
from uuid import UUID
from sqlmodel import Field, Relationship
from sqlalchemy import Column, Float  # Add this
from sqlalchemy.dialects.postgresql import ARRAY  # Add this
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

    # Fix: Add sa_column for vector embedding
    embedding: Optional[List[float]] = Field(
        default=None,
        sa_column=Column(ARRAY(Float))
    )

    # Source tracking
    file_url: Optional[str] = Field(default=None)
    uploaded_by: Optional[UUID] = Field(foreign_key="user.id")
    doc_interactions: List["DocumentInteraction"] = Relationship(back_populates="document")