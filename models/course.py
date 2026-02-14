from datetime import timezone, datetime
from enum import Enum
from typing import Optional, List

from sqlmodel import Field, SQLModel, Relationship
from uuid import UUID, uuid4
from .professor import Professor

class CourseStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    ARCHIVED = "ARCHIVED"

class Course(SQLModel, table=True):
    course_id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    title: str = Field(index=True)
    description: str
    credits: int = Field(default=4)
    professor_id: UUID = Field(foreign_key="professor.user_id", index=True)
    status: CourseStatus = Field(default=CourseStatus.ACTIVE, index=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    professor: Professor = Relationship(back_populates="courses")
    enrollements: List["Enrollment"] = Relationship(back_populates="course")
    course_materials: List["CourseMaterial"] = Relationship(back_populates="course")
    grades: List["Grade"] = Relationship(back_populates="course")
