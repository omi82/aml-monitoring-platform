from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.models.base_model import TimestampMixin


class Device(Base, TimestampMixin):
    __tablename__ = "dim_device"

    device_key: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    device_id: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
    )

    device_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    operating_system: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    browser: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    ip_address: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )