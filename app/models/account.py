from datetime import date

from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base
from app.models.base_model import TimestampMixin


class Account(TimestampMixin, Base):
    __tablename__ = "dim_account"

    account_key: Mapped[int] = mapped_column(
        primary_key=True
    )

    account_number: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        nullable=False,
        index=True,
    )

    customer_id: Mapped[str] = mapped_column(
        ForeignKey("dim_customer.customer_id"),
        nullable=False,
        index=True,
    )

    account_type: Mapped[str] = mapped_column(
        String(30)
    )

    currency: Mapped[str] = mapped_column(
        String(10)
    )

    status: Mapped[str] = mapped_column(
        String(20)
    )

    opened_date: Mapped[date] = mapped_column(
        Date
    )

    customer = relationship(
        "Customer",
        back_populates="accounts",
    )

    transactions = relationship(
        "Transaction",
        back_populates="account",
    )