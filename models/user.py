from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from uuid import UUID, uuid4

class UserBase(SQLModel):
    full_name: str
    email: str = Field(unique=True, index=True)
    hashed_password: str

class User(UserBase, table=True):
    user_id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    student: Optional["Student"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={"uselist": False}
    )