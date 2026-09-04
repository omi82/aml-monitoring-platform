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

    # --------------------------------------------------
    # Customer
    # --------------------------------------------------

    customer_id: Mapped[str | None] = mapped_column(
        ForeignKey("dim_customer.customer_id"),
        nullable=True,
        index=True,
    )

    # --------------------------------------------------
    # Alert
    # --------------------------------------------------

    alert_key: Mapped[int | None] = mapped_column(
        ForeignKey("fact_alert.alert_key"),
        unique=True,
        nullable=True,
    )

    # --------------------------------------------------
    # Investigation
    # --------------------------------------------------

    investigator: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    priority: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="Open",
        nullable=False,
    )

    comments: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # --------------------------------------------------
    # Audit / Assignment
    # --------------------------------------------------

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

    # --------------------------------------------------
    # Relationships
    # --------------------------------------------------

    customer = relationship(
        "Customer",
        back_populates="cases",
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