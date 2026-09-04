from sqlalchemy import Boolean
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base
from app.models.base_model import TimestampMixin


class Customer(TimestampMixin, Base):
    __tablename__ = "dim_customer"

    customer_key: Mapped[int] = mapped_column(
        primary_key=True
    )

    customer_id: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        nullable=False,
        index=True,
    )

    full_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    gender: Mapped[str] = mapped_column(
        String(20)
    )

    age: Mapped[int] = mapped_column(
        Integer
    )

    occupation: Mapped[str] = mapped_column(
        String(100)
    )

    annual_income: Mapped[float] = mapped_column(
        Numeric(15, 2)
    )

    kyc_status: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    risk_category: Mapped[str] = mapped_column(
        String(20),
        default="LOW",
    )

    accounts = relationship(
        "Account",
        back_populates="customer",
    )

    transactions = relationship(
        "Transaction",
        back_populates="customer",
    )