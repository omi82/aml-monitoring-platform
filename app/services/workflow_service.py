from app.services.audit_service import AuditService
from app.services.case_service import CaseService
from app.services.timeline_service import TimelineService
from app.core.workflow import is_valid_transition


class WorkflowService:

    def __init__(self, db):

        self.db = db
        self.case_service = CaseService(db)
        self.timeline_service = TimelineService(db)
        self.audit_service = AuditService(db)

    def change_status(
        self,
        case_id,
        new_status,
        username,
    ):

        case = self.case_service.get_case_by_id(case_id)

        if case is None:
            return None

        if not is_valid_transition(case.status, new_status):
            raise ValueError(       
                 f"Cannot change status from "
                 f"{case.status} to {new_status}"
    )

        old_status = case.status

        case.status = new_status

        updated_case = (
            self.case_service.repository.update(case)
        )

        self.timeline_service.create_entry(
            case_id=case.case_id,
            action="Status Changed",
            performed_by=username,
            old_value=old_status,
            new_value=new_status,
        )

        self.audit_service.log(
            username=username,
            action="STATUS_CHANGED",
            entity="Case",
            entity_id=str(case.case_id),
            details=f"{old_status} → {new_status}",
        )

        return updated_case

    def add_comment(
        self,
        case_id,
        comment,
        username,
    ):

        case = self.case_service.get_case_by_id(case_id)

        if case is None:
            return None

        updated_case = (
            self.case_service.repository.add_comment(
                case,
                comment,
            )
        )

        self.timeline_service.create_entry(
            case_id=case.case_id,
            action="Comment Added",
            performed_by=username,
            new_value=comment,
        )

        self.audit_service.log(
            username=username,
            action="COMMENT_ADDED",
            entity="Case",
            entity_id=str(case.case_id),
            details=comment,
        )

        return updated_case