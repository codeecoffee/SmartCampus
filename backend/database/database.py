from sqlmodel import SQLModel, create_engine, Session
from core.config import settings

import models

engine = create_engine(
    settings.database_url,
    echo=True
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session