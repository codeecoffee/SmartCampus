from enum import Enum
from uuid import UUID
from typing import TYPE_CHECKING, Optional
from datetime import datetime, timezone
from sqlmodel import Field, Relationship
from .base import StandaloneModel

if TYPE_CHECKING:
    from .user import User

class NotificationType(str, Enum):
    ACADEMIC_UPDATE = "academic_update"
    ANNOUNCEMENT = "announcement"
    DEADLINE = "deadline"

class DeliveryStatus(str, Enum):
    PENDING = "pending"
    DELIVERED = "delivered"
    FAILED = "failed"

class Notification(StandaloneModel, table=True):
    __tablename__ = "notification"
    type: NotificationType = Field(index=True)
    title: str
    message: str
    source_entity: Optional[str] = Field(default=None)
    source_entity_id: Optional[UUID] = Field(default=None)
    priority: int = Field(default=1, ge=1, le=5)

class UserNotification(StandaloneModel, table=True):
    __tablename__ = "user_notification"

    notification_id: UUID = Field(foreign_key="notification.id", index=True)
    user_id: UUID = Field(foreign_key="user.id", index=True)
    delivered_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    read_at: Optional[datetime] = Field(default=None)
    delivery_status: DeliveryStatus = Field(default=DeliveryStatus.PENDING, index=True)

    user: "User" = Relationship(back_populates="notifications")