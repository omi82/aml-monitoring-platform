from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.models.base_model import TimestampMixin

class Country(Base, TimestampMixin):
    __tablename__ = "dim_country"

    country_key: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    country_name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    risk_level: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    is_high_risk: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )