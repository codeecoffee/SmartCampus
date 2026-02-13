from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID
from .user import User

class Student(SQLModel, table=True):
    user_id: UUID = Field(foreign_key="user.user_id", primary_key=True)
    registration_number: str = Field(unique=True)
    major: str
    gpa: float

    user: "User" = Relationship(back_populates="students")