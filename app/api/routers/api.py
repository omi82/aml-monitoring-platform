from fastapi import APIRouter

from app.api.routers.health import router as health_router
from app.api.routers.auth import router as auth_router
from app.api.routers.alerts import router as alerts_router
from app.api.routers.cases import router as cases_router
from app.api.routers.customers import router as customers_router
from app.api.routers.dashboard import router as dashboard_router
from app.api.routers.audit import router as audit_router
from app.api.routers.timeline import router as timeline_router
from app.api.routers.case_alerts import router as case_alert_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(health_router)
api_router.include_router(auth_router)
api_router.include_router(alerts_router)
api_router.include_router(cases_router)
api_router.include_router(customers_router)
api_router.include_router(dashboard_router)
api_router.include_router(audit_router)
api_router.include_router(timeline_router)
api_router.include_router(case_alert_router)