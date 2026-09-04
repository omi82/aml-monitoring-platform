from sqlalchemy import ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.models.base_model import TimestampMixin
from sqlalchemy import UniqueConstraint


class Alert(Base, TimestampMixin):
    __tablename__ = "fact_alert"

    __table_args__ = (
        UniqueConstraint("transaction_id", "rule_name", name="uq_transaction_rule"),
    )

    alert_key: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    transaction_id: Mapped[str] = mapped_column(
        ForeignKey("fact_transaction.transaction_id"),
        nullable=False,
        index=True,
    )

    rule_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    severity: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    risk_score: Mapped[float] = mapped_column(
        Numeric(5, 2),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="Open",
    )

    reason: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    transaction = relationship(
        "Transaction",
        back_populates="alerts",
    )

    case = relationship(
        "Case",
        back_populates="alert",
        uselist=False,
    )