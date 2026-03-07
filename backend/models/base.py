from datetime import datetime, timezone
from typing import Optional
from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4

#universal - timestamp
class TimestampMixin(SQLModel):
    created_at: datetime = Field(default_factory= lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory= lambda: datetime.now(timezone.utc))

#primary key mixin
class UUIDPKMixin(SQLModel):
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
class StandaloneModel(UUIDPKMixin, TimestampMixin):
    pass
class TimestampOnlyModel(TimestampMixin):
    pass