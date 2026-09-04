from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.api.schemas.timeline import TimelineResponse
from app.services.timeline_service import TimelineService

router = APIRouter(
    prefix="/timeline",
    tags=["Timeline"],
)


@router.get(
    "",
    response_model=List[TimelineResponse],
)
def get_timeline(
    db: Session = Depends(get_db),
):

    service = TimelineService(db)

    return service.get_all()


@router.get(
    "/{case_id}",
    response_model=List[TimelineResponse],
)
def get_case_timeline(
    case_id: UUID,
    db: Session = Depends(get_db),
):

    service = TimelineService(db)

    return service.get_case_timeline(case_id)