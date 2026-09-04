from app.models.case_alert import CaseAlert
from app.repositories.case_alert_repository import (
    CaseAlertRepository,
)


class CaseAlertService:

    def __init__(self, db):

        self.repository = CaseAlertRepository(db)

    def link_alert(
        self,
        case_id,
        alert_key,
        linked_by="System",
    ):

        if self.repository.exists(
            case_id,
            alert_key,
        ):
            return None

        mapping = CaseAlert(
            case_id=case_id,
            alert_key=alert_key,
            linked_by=linked_by,
        )

        return self.repository.create(mapping)

    def get_case_alerts(
        self,
        case_id,
    ):

        return self.repository.get_alerts_by_case(case_id)