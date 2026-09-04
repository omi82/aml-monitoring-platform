from sqlalchemy.orm import Session

from app.models.case_alert import CaseAlert


class CaseAlertRepository:

    def __init__(self, db: Session):

        self.db = db

    def create(
        self,
        mapping: CaseAlert,
    ):

        self.db.add(mapping)
        self.db.commit()
        self.db.refresh(mapping)

        return mapping

    def get_alerts_by_case(
        self,
        case_id,
    ):

        return (
            self.db.query(CaseAlert)
            .filter(CaseAlert.case_id == case_id)
            .all()
        )

    def get_cases_by_alert(
        self,
        alert_key,
    ):

        return (
            self.db.query(CaseAlert)
            .filter(CaseAlert.alert_key == alert_key)
            .all()
        )

    def exists(
        self,
        case_id,
        alert_key,
    ):

        return (
            self.db.query(CaseAlert)
            .filter(
                CaseAlert.case_id == case_id,
                CaseAlert.alert_key == alert_key,
            )
            .first()
            is not None
        )