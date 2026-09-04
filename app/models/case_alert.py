import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.models.base_model import TimestampMixin


class CaseAlert(Base, TimestampMixin):
    __tablename__ = "fact_case_alert"

    case_alert_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    case_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("fact_case.case_id"),
        nullable=False,
        index=True,
    )

    alert_key: Mapped[int] = mapped_column(
        ForeignKey("fact_alert.alert_key"),
        nullable=False,
        index=True,
    )

    linked_by: Mapped[str] = mapped_column(
        nullable=False,
        default="System",
    )