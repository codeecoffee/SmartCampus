from datetime import timezone, datetime
from enum import Enum
from typing import Optional, List, TYPE_CHECKING
from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel, Relationship
from .base import StandaloneModel

if TYPE_CHECKING:
    from .attendance import AttendanceSession
    from .courseMaterial import CourseMaterial
    from .enrollment import Enrollment
    from .professor import Professor
class CourseStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    ARCHIVED = "archived"

class Course(StandaloneModel, table=True):
    __tablename__ = "course"
    title: str = Field(index=True)
    description: str
    code: str = Field(unique=True, index=True)
    credits: int = Field(default=4)
    status: CourseStatus = Field(default=CourseStatus.ACTIVE, index=True)
    professor_id: Optional[UUID] = Field(default=None, foreign_key="professor.user_id")

    professor: Optional["Professor"] = Relationship(back_populates="courses")
    enrollments: List["Enrollment"] = Relationship(back_populates="course")
    materials: List["CourseMaterial"] = Relationship(back_populates="course")
    attendance_sessions: List["AttendanceSession"] = Relationship(back_populates="course")
