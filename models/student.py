from typing import TYPE_CHECKING, Any, Dict,List, Optional
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlmodel import SQLModel, Field, Relationship, Column, JSON

from models.base import TimestampOnlyModel

if TYPE_CHECKING:
    from .attendance import AttendanceRecord
    from .enrollment import Enrollment
    from .user import User

class Student(TimestampOnlyModel, table=True):
    __tablename__ = "student"
     # user_id: UUID = Field(foreign_key='user.id', primary_key=True, ondelete="CASCADE")
    user_id: UUID = Field(
        sa_column=Column(ForeignKey("user.id",ondelete="CASCADE"), primary_key=True),
    )
    registration_number: str = Field(unique=True, index=True)
    major: Optional[str] = Field(default= None, index=True)
    gpa: Optional[float] = Field(default=0.0)
    # metadata: Optional[Dict[str, Any]] = Field(default=None)
    student_metadata: Optional[Dict[str, Any]] = Field(
        default=None, sa_column=Column("student_metadata", JSON, nullable=True)
    )
    user: "User" = Relationship(back_populates="student")
    enrollments: List["Enrollment"] = Relationship(back_populates="student")
    attendance_records: List["AttendanceRecord"] = Relationship(back_populates="student")