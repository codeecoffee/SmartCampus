from datetime import datetime, timezone
from typing import Optional
from enum import Enum
from sqlmodel import Field, Relationship
from uuid import UUID
from models.base import StandaloneModel
from models.enrollment import Enrollment

class AssessmentType(str, Enum):
    EXAM = "exam"
    ASSIGNMENT = "assignment"
    PROJECT = "project"
    PARTICIPATION = "participation"

class Grade(StandaloneModel, table=True):
    enrollment_id: UUID = Field(foreign_key="enrollment.id")
    # AI analyzes grade distributions by type to suggest study focus
    assessment_type: AssessmentType = Field()
    value: float = Field(default=0)

    #AI-generated or Professor-written
    feedback: Optional[str] = Field()

    #When graded (for trend analysis: "improving over time ?")
    graded_at: datetime = Field(default_factory= lambda: datetime.now(timezone.utc))

    enrollment: Enrollment = Relationship(back_populates="grade")