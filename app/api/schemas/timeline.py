from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class TimelineResponse(BaseModel):

    timeline_id: UUID
    case_id: UUID
    action: str
    performed_by: str
    old_value: str | None = None
    new_value: str | None = None
    comments: str | None = None
    created_at: datetime

    model_config = {
        "from_attributes": True
    }