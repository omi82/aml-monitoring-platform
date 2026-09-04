import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Case(Base):

    __tablename__ = "fact_case"

    case_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    alert_key: Mapped[int] = mapped_column(
        ForeignKey("fact_alert.alert_key"),
        unique=True,
        nullable=False,
    )

    investigator: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="Open",
    )

    priority: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    comments: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    closed_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    assigned_by: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    assigned_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    alert = relationship(
        "Alert",
        back_populates="case",
    )


    timeline = relationship(
        "CaseTimeline",
        back_populates="case",
        cascade="all, delete-orphan",
    )