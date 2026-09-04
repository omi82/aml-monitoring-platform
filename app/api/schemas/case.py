from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class CaseResponse(BaseModel):

    case_id: UUID
    alert_key: int
    investigator: str | None = None
    priority: str
    status: str
    comments: str | None = None
    created_at: datetime
    closed_at: datetime | None = None

    model_config = {
        "from_attributes": True
    }