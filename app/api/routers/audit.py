from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.api.schemas.audit import AuditResponse
from app.core.permissions import require_roles
from app.services.audit_service import AuditService

router = APIRouter(
    prefix="/audit",
    tags=["Audit"],
)


@router.get(
    "",
    response_model=List[AuditResponse],
)
def get_audit_logs(
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles("Admin"),
    ),
):

    service = AuditService(db)

    return service.get_all_logs()


@router.get(
    "/user/{username}",
    response_model=List[AuditResponse],
)
def get_user_logs(
    username: str,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles("Admin"),
    ),
):

    service = AuditService(db)

    return service.get_user_logs(username)