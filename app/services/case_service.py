from app.models.case import Case
from app.repositories.case_repository import CaseRepository


class CaseService:

    def __init__(self, db):

        self.repository = CaseRepository(db)

    def calculate_priority(self, risk_score):
        """
        Calculate case priority based on risk score.
        """

        if risk_score >= 95:
            return "Critical"

        if risk_score >= 85:
            return "High"

        if risk_score >= 70:
            return "Medium"

        return "Low"

    def case_exists(self, alert_key):
        """
        Check whether a case already exists
        for the given alert.
        """

        return (
            self.repository.get_by_alert(alert_key)
            is not None
        )

    def create_case(self, alert):
        """
        Create a new investigation case
        for the given alert.
        """

        existing = self.repository.get_by_alert(
            alert.alert_key
        )

        if existing:
            return existing

        case = Case(
            alert_key=alert.alert_key,
            priority=self.calculate_priority(
                alert.risk_score
            ),
            status="Open",
        )

        return self.repository.create(case)
    
    def get_all_cases(
        self,
        filters,
    ):
        return self.repository.get_all(filters)

    def get_open_cases(self):
        """
        Return all open investigation cases.
        """

        return self.repository.get_open_cases()

    def get_case_by_id(self, case_id):
        """
        Return a case by its ID.
        """

        return self.repository.get_by_id(case_id)

    def assign_case(
        self,
        case_id,
        investigator,
        assigned_by,
    ):

        case = self.repository.get_by_id(case_id)

        if case is None:
            return None

        return self.repository.assign_case(
            case,
            investigator,
            assigned_by,
        )