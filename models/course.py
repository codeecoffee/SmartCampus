from datetime import timezone, datetime
from enum import Enum
from typing import Optional, List

from sqlmodel import Field, SQLModel, Relationship
from uuid import UUID, uuid4

from .base import StandaloneModel
from .professor import Professor

class CourseStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    ARCHIVED = "ARCHIVED"

class Course(StandaloneModel, table=True):
    title: str = Field(index=True)
    description: str = Field()
    code: str = Field(unique=True)
    credits: int = Field(default=4)
    status: CourseStatus = Field(default=CourseStatus.ACTIVE, index=True)

    professor: Professor = Relationship(back_populates="courses")
    enrollements: List["Enrollment"] = Relationship(back_populates="course")
    materials: List["CourseMaterial"] = Relationship(back_populates="course")
    # grades: List["Grade"] = Relationship(back_populates="course")
