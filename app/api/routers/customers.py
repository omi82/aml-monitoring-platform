from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.api.schemas.customer import (
    CustomerListResponse,
    CustomerResponse,
)
from app.api.schemas.customer_filter import CustomerFilter
from app.api.schemas.customer_overview import (
    CustomerOverviewResponse,
)
from app.auth.dependencies import get_current_user
from app.core.permissions import require_roles
from app.services.audit_service import AuditService
from app.services.customer_overview_service import (
    CustomerOverviewService,
)
from app.services.customer_service import CustomerService


router = APIRouter(
    prefix="/customers",
    tags=["Customers"],
)


@router.get(
    "",
    response_model=CustomerListResponse,
)
def get_customers(
    page: int = Query(1, ge=1),
    size: int = Query(20, ge=1, le=100),
    country: str | None = None,
    risk_level: str | None = None,
    customer_type: str | None = None,
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

    filters = CustomerFilter(
        page=page,
        size=size,
        country=country,
        risk_level=risk_level,
        customer_type=customer_type,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    service = CustomerService(db)

    return service.get_all_customers(filters)


@router.get(
    "/{customer_id}",
    response_model=CustomerResponse,
)
def get_customer(
    customer_id: str,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Admin",
            "Investigator",
            "Compliance Officer",
        )
    ),
):

    service = CustomerService(db)

    customer = service.get_customer_by_id(
        customer_id
    )

    if customer is None:

        raise HTTPException(
            status_code=404,
            detail="Customer not found",
        )

    AuditService(db).log_action(
        current_user,
        action="VIEW",
        entity="Customer",
        entity_id=customer_id,
        details="Viewed customer profile",
    )

    return customer


@router.get(
    "/{customer_id}/overview",
    response_model=CustomerOverviewResponse,
)
def get_customer_overview(
    customer_id: str,
    db: Session = Depends(get_db),
):

    service = CustomerOverviewService(db)

    overview = service.get_overview(
        customer_id
    )

    if overview is None:

        raise HTTPException(
            status_code=404,
            detail="Customer not found",
        )

    return overview