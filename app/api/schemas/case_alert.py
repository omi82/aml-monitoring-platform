from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class CaseAlertResponse(BaseModel):

    case_alert_id: UUID
    case_id: UUID
    alert_key: int
    linked_by: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }