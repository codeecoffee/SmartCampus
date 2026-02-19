from pgvector.sqlalchemy import Vector
from datetime import datetime, timezone

from sqlalchemy.orm import Relationship

from models import Course
from models.base import StandaloneModel
from uuid import UUID
from sqlmodel import Field
from typing import Optional, List
class CourseMaterial(StandaloneModel, table=True):
    course_id: UUID = Field(foreign_key="course.id")
    title: str = Field()
    content: str = Field()
    #TODO: implement the get_vector_column in the database.py
    embedding: Optional[List[float]] = Field(
        sa_column=get_vector_column(nullable=True)
    )
    file_url: Optional[str] = Field()
    file_type: str = Field()

    indexed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    course: Course = Relationship(back_populates="materials")