from sqlmodel import Field, SQLModel, Relationship
from uuid import UUID, uuid4
from .professor import Professor

class Course(SQLModel, table=True):
    course_id: