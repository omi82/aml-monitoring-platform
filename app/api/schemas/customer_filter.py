from typing import Literal

from pydantic import BaseModel


class CustomerFilter(BaseModel):
    page: int = 1
    size: int = 20

    country: str | None = None
    risk_level: str | None = None
    customer_type: str | None = None

    sort_by: Literal[
        "customer_name",
        "country",
        "risk_level",
        "created_at",
    ] = "created_at"

    sort_order: Literal[
        "asc",
        "desc",
    ] = "desc"