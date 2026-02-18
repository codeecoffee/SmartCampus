from datetime import datetime
from typing import Optional
from models.student import Student
from models
from models.base import StandaloneModel
from sqlmodel import Field, Relationship
from uuid import UUID
from typing import Optional, List

class Enrollment(StandaloneModel,table=True):
    student_id: UUID = Field(foreign_key="students.user_id")
    course_id: UUID = Field(foreign_key="course.id")

    status:
    completed_at: Optional[datetime] = Field(default=None)

    student: Student = Relationship(back_populates="enrollments")
    course: Course = Relationship(back_populates="enrollments")
    grades: List["Grade"] = Relationship(back_populates="enrollment")
