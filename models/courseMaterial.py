from datetime import datetime, timezone
from enum import Enum
from typing import TYPE_CHECKING, List, Optional
from uuid import UUID
from sqlmodel import Field, Relationship
from models.base import StandaloneModel

if TYPE_CHECKING:
    from .course import Course
class MaterialType(str, Enum):
    PDF = "pdf"
    DOCX = "docx"
    LINK = "link"
    NOTE = "note"

class CourseMaterial(StandaloneModel, table= True):
    __tablename__ = "course_material"

    course_id: UUID = Field(foreign_key="course.id", index=True)
    title: str
    content: str
    embedding: Optional[List[float]] = Field(default=None)
    file_url: Optional[str] = Field(default=None)
    file_type: MaterialType = Field(index=True)
    indexed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc, index=True))
    course: "Course" = Relationship(back_populates="materials")