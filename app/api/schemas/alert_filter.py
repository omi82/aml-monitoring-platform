from typing import Literal

from pydantic import BaseModel


class AlertFilter(BaseModel):
    page: int = 1
    size: int = 20

    severity: str | None = None
    status: str | None = None
    rule_name: str | None = None

    min_risk_score: float | None = None
    max_risk_score: float | None = None

    sort_by: Literal[
        "risk_score",
        "created_at",
        "severity",
    ] = "created_at"

    sort_order: Literal[
        "asc",
        "desc",
    ] = "desc"