from datetime import datetime, timezone
from enum import Enum
from typing import Optional, TYPE_CHECKING
from uuid import UUID
from sqlmodel import Field, Relationship
from models.base import StandaloneModel

if TYPE_CHECKING:
    from .enrollment import Enrollment

class AssessmentType(str, Enum):
    EXAM = "exam"
    ASSIGNMENT = "assignment"
    PROJECT = "project"
    PARTICIPATION = "participation"

class Grade(StandaloneModel, table=True):
    __tablename__ = 'grade'
    enrollment_id: UUID = Field(foreign_key="enrollment.id",index=True)

    # AI analyzes grade distributions by type to suggest study focus
    assessment_type: AssessmentType = Field(index=True)
    value: float = Field(default=0)

    #AI-generated or Professor-written
    feedback: Optional[str] = Field(default=None)

    #When graded (for trend analysis: "improving over time ?")
    graded_at: datetime = Field(default_factory= lambda: datetime.now(timezone.utc), index=True)

    enrollment: "Enrollment" = Relationship(back_populates="grades")