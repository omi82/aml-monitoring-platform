from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class AuditResponse(BaseModel):

    audit_id: UUID
    username: str
    action: str
    entity: str
    entity_id: str | None = None
    details: str | None = None
    created_at: datetime

    model_config = {
        "from_attributes": True
    }