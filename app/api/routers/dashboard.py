from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.api.schemas.dashboard import DashboardSummaryResponse, ChartResponse
from app.services.audit_service import AuditService
from app.services.dashboard_service import DashboardService
from app.auth.dependencies import get_current_user
from app.core.permissions import require_roles

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get(
    "/summary",
    response_model=DashboardSummaryResponse,
)
def get_dashboard_summary(
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Admin",  "Compliance Officer",)),
):

    service = DashboardService(db)

    AuditService(db).log_action(
        current_user,
        action="VIEW",
        entity="Dashboard",
        details="Viewed dashboard summary",
    )

    return service.get_summary()

@router.get("/recent-alerts")
def get_recent_alerts(
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Admin", "Compliance Officer")),
):



    AuditService(db).log_action(
        current_user,
        action="VIEW",
        entity="Dashboard",
        details="Viewed recent alerts",
    )

    return DashboardService(db).get_recent_alerts()


@router.get("/recent-cases")
def get_recent_cases(
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Admin", "Compliance Officer")),
):

    AuditService(db).log_action(
        current_user,
        action="VIEW",
        entity="Dashboard",
        details="Viewed recent cases",
    )

    return DashboardService(db).get_recent_cases()


@router.get(
    "/alerts-by-severity",
    response_model=list[ChartResponse],
)
def get_alerts_by_severity(
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Admin", "Compliance Officer")),
):

    rows = DashboardService(db).get_alerts_by_severity()

    AuditService(db).log_action(
        current_user,
        action="VIEW",
        entity="Dashboard",
        details="Viewed alerts by severity",
    )

    return [
        {
            "label": row.severity,
            "count": row.count,
        }
        for row in rows
    ]


@router.get(
    "/alerts-by-rule",
    response_model=list[ChartResponse],
)
def get_alerts_by_rule(
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Admin", "Compliance Officer")),
):

    rows = DashboardService(db).get_alerts_by_rule()

    AuditService(db).log_action(
        current_user,
        action="VIEW",
        entity="Dashboard",
        details="Viewed alerts by rule",
    )

    return [
        {
            "label": row.rule_name,
            "count": row.count,
        }
        for row in rows
    ]


@router.get(
    "/risk-distribution",
    response_model=list[ChartResponse],
)
def get_risk_distribution(
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("Admin", "Compliance Officer")),
):

    rows = DashboardService(db).get_risk_distribution()
    AuditService(db).log_action(
        current_user,
        action="VIEW",
        entity="Dashboard",
        details="Viewed risk distribution",
    )

    return [
        {
            "label": row.risk_category,
            "count": row.count,
        }
        for row in rows
    ]