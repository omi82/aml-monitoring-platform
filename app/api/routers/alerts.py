from typing import List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.api.schemas.alert import AlertResponse
from app.auth.dependencies import get_current_user
from app.core.permissions import require_roles
from app.services.alert_service import AlertService
from app.services.audit_service import AuditService
from fastapi import Query

from app.api.schemas.alert_filter import AlertFilter

router = APIRouter(
    prefix="/alerts",
    tags=["Alerts"],
)


@router.get(
    "",
    response_model=List[AlertResponse],
)
def get_alerts(
    page: int = Query(1),
    size: int = Query(20),
    severity: str | None = None,
    status: str | None = None,
    rule_name: str | None = None,
    min_risk_score: float | None = None,
    max_risk_score: float | None = None,
    sort_by: str = "created_at",
    sort_order: str = "desc",
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Admin",
            "Investigator",
        )
    ),
):

    filters = AlertFilter(
        page=page,
        size=size,
        severity=severity,
        status=status,
        rule_name=rule_name,
        min_risk_score=min_risk_score,
        max_risk_score=max_risk_score,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    service = AlertService(db)

    return service.get_all_alerts(filters)

@router.get(
    "/open",
    response_model=List[AlertResponse],
)
def get_open_alerts(
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Admin",
            "Investigator",
            "Auditor",
        )
    ),
):
    service = AlertService(db)

    # Audit Log
    AuditService(db).log_action(
        current_user=current_user,
        action="VIEW",
        entity="Alerts",
        details="Viewed open alerts",
    )

    return service.get_open_alerts()