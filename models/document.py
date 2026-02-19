from typing import Optional, List
from uuid import UUID
from pgvector.sqlalchemy import Vector
from sqlmodel import Field, Relationship
from enum import Enum
from models.base import StandaloneModel

class DocumentType(str, Enum):
    SYLLABUS="syllabus"
    REGULATION="regulation"
    GUIDELINE="guideline"
    RESEARCH="research"
class Document(StandaloneModel, table=True):
    title: str = Field(index=True)
    doc_type: DocumentType = Field()
    content: str = Field()

    #Vector search
    embedding: Optional[List[float]] = Field(default=None)

    #Source tracking
    file_url: Optional[str]= Field()
    uploaded_by: Optional[UUID] = Field(foreign_key="user.user_id")

    doc_interactions: List["DocInteraction"] = Relationship(back_populates="document")