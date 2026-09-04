from app.repositories.alert_repository import AlertRepository
from app.services.case_service import CaseService


class CaseCreationService:

    def __init__(self, db):

        self.db = db
        self.case_service = CaseService(db)
        self.alert_repository = AlertRepository(db)

    def create_cases_for_new_alerts(self):

        alerts = self.alert_repository.get_open_alerts()

        created = 0

        for alert in alerts:

            if alert.risk_score < 90:
                continue

            if self.case_service.case_exists(alert.alert_key):
                continue

            self.case_service.create_case(alert)

            created += 1

        print(
            f"Created {created} investigation cases."
        )

        return created