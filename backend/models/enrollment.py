from datetime import datetime, timezone
from enum import Enum
from typing import Optional, List, TYPE_CHECKING
from uuid import UUID
from sqlmodel import Field, Relationship
from models.base import StandaloneModel

if TYPE_CHECKING:
    from .course import Course
    from .grade import Grade
    from .student import Student

class EnrollmentStatus(str, Enum):
    ENROLLED = 'enrolled'
    DROPPED = 'dropped'
    COMPLETED = 'completed'
    WAITLISTED = 'waitlisted'

class Enrollment(StandaloneModel, table=True):
    __tablename__ = 'enrollment'

    student_id: Optional[UUID] = Field(foreign_key="student.user_id", index=True)
    course_id: Optional[UUID] = Field(foreign_key="course.id", index=True)
    status: EnrollmentStatus = Field(default=EnrollmentStatus.ENROLLED, index=True)
    enrollment_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    last_grade_updated_at: datetime = Field(default=None)

    student: "Student" = Relationship(back_populates="enrollments")
    course: "Course" = Relationship(back_populates="enrollments")
    grade: List["Grade"] = Relationship(back_populates="enrollment")

