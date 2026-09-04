from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base
from app.models.base_model import TimestampMixin


class Transaction(TimestampMixin, Base):
    """
    Transaction Fact Table
    """

    __tablename__ = "fact_transaction"

    transaction_key: Mapped[int] = mapped_column(
        primary_key=True
    )

    transaction_id: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        nullable=False,
        index=True,
    )

    account_number: Mapped[str] = mapped_column(
        ForeignKey("dim_account.account_number"),
        nullable=False,
        index=True,
    )

    customer_id: Mapped[str] = mapped_column(
        ForeignKey("dim_customer.customer_id"),
        nullable=False,
        index=True,
    )

    amount: Mapped[float] = mapped_column(
        Numeric(15, 2),
        nullable=False,
    )

    transaction_type: Mapped[str] = mapped_column(
        String(30)
    )

    channel: Mapped[str] = mapped_column(
        String(30)
    )

    merchant_category: Mapped[str] = mapped_column(
        String(50)
    )

    country: Mapped[str] = mapped_column(
        String(50)
    )

    status: Mapped[str] = mapped_column(
        String(20)
    )

    transaction_timestamp: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    account = relationship(
        "Account",
        back_populates="transactions",
    )

    customer = relationship(
        "Customer",
        back_populates="transactions",
    )

    alerts = relationship(
        "Alert",
        back_populates="transaction",
    )