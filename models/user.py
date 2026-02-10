from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from uuid import UUID, uuid4

class UserBase(SQLModel):
    full_name: str
    email: str = Field(unique=True, index=True)

class User(UserBase, table=True):
    user_id: Optional[UUID] = Fieeld(default_factory=uuid4, primary_key=True)