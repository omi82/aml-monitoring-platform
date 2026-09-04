from typing import List

from pydantic import BaseModel

from app.api.schemas.customer import CustomerResponse
from app.api.schemas.alert import AlertResponse
from app.api.schemas.case import CaseResponse
from app.api.schemas.timeline import TimelineResponse


class CustomerOverviewResponse(BaseModel):

    customer: CustomerResponse

    alerts: List[AlertResponse]

    cases: List[CaseResponse]

    timeline: List[TimelineResponse]

    model_config = {
        "from_attributes": True
    }