from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class CaseResponse(BaseModel):

    case_id: UUID

    customer_id: str | None = None

    alert_key: int | None = None

    investigator: str | None = None

    priority: str

    status: str

    comments: str | None = None

    created_at: datetime

    closed_at: datetime | None = None

    assigned_by: str | None = None

    assigned_at: datetime | None = None

    model_config = {
        "from_attributes": True
    }


# ==================================================
# CASE LIST / PAGINATION RESPONSE
# ==================================================

class CaseListResponse(BaseModel):

    items: list[CaseResponse]

    total: int

    page: int

    size: int