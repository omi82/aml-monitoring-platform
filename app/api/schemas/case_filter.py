from typing import Literal

from pydantic import BaseModel


class CaseFilter(BaseModel):
    page: int = 1
    size: int = 20

    status: str | None = None
    priority: str | None = None
    investigator: str | None = None

    sort_by: Literal[
        "created_at",
        "priority",
        "status",
    ] = "created_at"

    sort_order: Literal[
        "asc",
        "desc",
    ] = "desc"