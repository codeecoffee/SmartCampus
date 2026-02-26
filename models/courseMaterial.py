from datetime import datetime, timezone
from enum import Enum
from typing import TYPE_CHECKING, List, Optional
from uuid import UUID
from sqlmodel import Field, Relationship
from sqlalchemy import Column, Float  # Add this import
from sqlalchemy.dialects.postgresql import ARRAY  # Add this import
from models.base import StandaloneModel

if TYPE_CHECKING:
    from .course import Course


class MaterialType(str, Enum):
    PDF = "pdf"
    DOCX = "docx"
    LINK = "link"
    NOTE = "note"


class CourseMaterial(StandaloneModel, table=True):
    __tablename__ = "course_material"

    course_id: UUID = Field(foreign_key="course.id", index=True)
    title: str
    content: str

    # Fix: Explicitly specify the SQLAlchemy column type for the list of floats
    embedding: Optional[List[float]] = Field(
        default=None,
        sa_column=Column(ARRAY(Float))  # This tells SQLModel how to store it
    )

    file_url: Optional[str] = Field(default=None)
    file_type: MaterialType = Field(index=True)

    # Also fix: index=True should be in Field(), not datetime.now()
    indexed_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        index=True  # Move index=True here
    )

    course: "Course" = Relationship(back_populates="materials")