from typing import Optional, List
from uuid import UUID
from pgvector.sqlalchemy import Vector
from sqlmodel import Field, Relationship

from models.base import StandaloneModel


class Document(StandaloneModel, table=True):
    title: str = Field(index=True)
    doc_type:
    content: str = Field()

    #Vector search
    embedding: Optional[List[float]] = Field(default=None)

    #Source tracking
    file_url: Optional[str]= Field()
    uploaded_by: Optional[UUID] = Field(foreign_key="user.user_id")

    doc_interactions: List["DocInteraction"] = Relationship(back_populates="document")