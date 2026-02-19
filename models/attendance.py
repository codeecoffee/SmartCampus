from sqlmodel import Field, Relationship
from typing import TYPE_CHECKING, List, Optional
from enum import Enum
from uuid import UUID
from datetime import datetime, timezone
from .base import StandaloneModel

if TYPE_CHECKING:
    from .course import Course
    from .student import Student

class AttendanceStatus(str, Enum):
    PRESENT = "present"
    ABSENT = "absent"
    LATE = "late"
    EXCUSED = "excused"
class AttendanceSession(StandaloneModel, table=True):
    __tablename__ = "attendance_session"

    course_id: UUID = Field(foreign_key="course.id", index=True)
    starts_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), index=True)
    ends_at: Optional[datetime] = Field(default=None)
    topic: Optional[str] = Field(default=None)

    course: "Course" = Relationship(back_populates="attendance_sessions")
    records: List["AttendanceRecord"] = Relationship(back_populates="session")
class AttendanceRecord(StandaloneModel, table=True):
    __tablename__ = "attendance_record"

    attendance_session_id: UUID = Field(foreign_key="attendance_session.id", index=True)
    student_id: UUID = Field(foreign_key="student.user_id", index=True)
    status: AttendanceStatus = Field(default=AttendanceStatus.PRESENT, index=True)
    marked_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), index=True)
    notes: Optional[str] = Field(default=None)

    session: "AttendanceSession" = Relationship(back_populates="records")
    student: "Student" = Relationship(back_populates="attendance_records")