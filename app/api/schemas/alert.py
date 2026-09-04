from pydantic import BaseModel
from datetime import datetime


class AlertResponse(BaseModel):

    alert_key: int
    transaction_id: str
    rule_name: str
    severity: str
    risk_score: int
    status: str
    reason: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }