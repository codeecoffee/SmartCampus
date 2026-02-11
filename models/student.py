from sqlmodel import Field, SQLModel,Relationship
from typing import Optional
from uuid import UUID

class Student(SQLModel, table=True):
    user_id: UUID = Field(foreign_key='user.user_id', primary_key=True)
    registration_number: str = Field(unique=True)
    major: str

    user:"User" = Relationship(back_populates="students")