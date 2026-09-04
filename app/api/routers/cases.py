from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.api.schemas.case import CaseResponse
from app.core.permissions import require_roles
from app.services.audit_service import AuditService
from app.services.case_service import CaseService
from app.api.schemas.assignment import AssignCaseRequest
from app.api.schemas.case_comment import CaseCommentRequest

from app.api.schemas.case_status import CaseStatusUpdate
from app.services.workflow_service import WorkflowService
from app.auth.dependencies import get_current_user
from fastapi import Query
from app.api.schemas.case_filter import CaseFilter

router = APIRouter(
    prefix="/cases",
    tags=["Cases"],
)


@router.get(
    "",
    response_model=List[CaseResponse],
)
def get_cases(
    page: int = Query(1),
    size: int = Query(20),
    status: str | None = None,
    priority: str | None = None,
    investigator: str | None = None,
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

    filters = CaseFilter(
        page=page,
        size=size,
        status=status,
        priority=priority,
        investigator=investigator,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    service = CaseService(db)

    AuditService(db).log_action(
        current_user=current_user,
        action="VIEW",
        entity="Cases",
        details="Viewed filtered case list",
    )

    return service.get_all_cases(filters)


@router.get(
    "/open",
    response_model=List[CaseResponse],
)
def get_open_cases(
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Admin",
            "Investigator",
        )
    ),
):
    service = CaseService(db)

    # Audit Log
    AuditService(db).log_action(
        current_user=current_user,
        action="VIEW",
        entity="Cases",
        details="Viewed open cases",
    )

    return service.get_open_cases()


@router.get(
    "/{case_id}",
    response_model=CaseResponse,
)
def get_case(
    case_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Admin",
            "Investigator",
        )
    ),
):
    service = CaseService(db)

    case = service.get_case_by_id(case_id)

    if case is None:
        raise HTTPException(
            status_code=404,
            detail="Case not found",
        )

    # Audit Log
    AuditService(db).log_action(
        current_user=current_user,
        action="VIEW",
        entity="Case",
        entity_id=str(case_id),
        details="Viewed case details",
    )

    return case


@router.patch(
    "/{case_id}/status",
    response_model=CaseResponse,
)
def update_case_status(
    case_id: UUID,
    request: CaseStatusUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    workflow = WorkflowService(db)

    try:

        case = workflow.change_status(
            case_id=case_id,
            new_status=request.status,
            username=current_user.username,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

    if case is None:
        raise HTTPException(
            status_code=404,
            detail="Case not found",
        )

    return case


@router.post(
    "/{case_id}/assign",
)
def assign_case(
    case_id: UUID,
    request: AssignCaseRequest,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Admin",
        )
    ),
):

    service = CaseService(db)

    case = service.assign_case(
        case_id,
        request.investigator,
        current_user.username,
    )

    if case is None:

        raise HTTPException(
            status_code=404,
            detail="Case not found",
        )

    AuditService(db).log_action(
        current_user,
        action="ASSIGN",
        entity="Case",
        entity_id=str(case_id),
        details=f"Assigned to {request.investigator}",
    )

    return {
        "message": "Case assigned successfully"
    }


@router.post(
    "/{case_id}/comment",
    response_model=CaseResponse,
)
def add_case_comment(
    case_id: UUID,
    request: CaseCommentRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    workflow = WorkflowService(db)

    case = workflow.add_comment(
        case_id=case_id,
        comment=request.comment,
        username=current_user.username,
    )

    if case is None:
        raise HTTPException(
            status_code=404,
            detail="Case not found",
        )

    return case