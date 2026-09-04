from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.api.schemas.case_alert import (
    CaseAlertResponse,
)
from app.services.case_alert_service import (
    CaseAlertService,
)

router = APIRouter(
    prefix="/case-alerts",
    tags=["Case Alerts"],
)


@router.get(
    "/{case_id}",
    response_model=List[CaseAlertResponse],
)
def get_case_alerts(
    case_id: UUID,
    db: Session = Depends(get_db),
):

    service = CaseAlertService(db)

    return service.get_case_alerts(case_id)