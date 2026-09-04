from typing import List

from pydantic import BaseModel

from app.api.schemas.customer import CustomerResponse
from app.api.schemas.account import AccountResponse
from app.api.schemas.transaction import TransactionResponse
from app.api.schemas.alert import AlertResponse
from app.api.schemas.case import CaseResponse
from app.api.schemas.timeline import TimelineResponse
from app.api.schemas.ai_summary import AISummaryResponse


class CustomerOverviewResponse(BaseModel):

    customer: CustomerResponse

    accounts: List[AccountResponse]

    transactions: List[TransactionResponse]

    alerts: List[AlertResponse]

    cases: List[CaseResponse]

    timeline: List[TimelineResponse]

    ai_summary: AISummaryResponse

    model_config = {
        "from_attributes": True
    }