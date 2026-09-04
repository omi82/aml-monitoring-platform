from uuid import UUID

from app.ai.summary_generator import SummaryGenerator
from app.repositories.case_repository import CaseRepository
from app.repositories.alert_repository import AlertRepository


class AIService:

    def __init__(self, db):

        self.case_repository = CaseRepository(db)
        self.alert_repository = AlertRepository(db)

    def generate_case_summary(
        self,
        case_id: UUID,
    ):

        case = self.case_repository.get_by_id(case_id)

        if case is None:
            return None

        alerts = self.alert_repository.get_by_case(case_id)

        summary = SummaryGenerator.generate(
            case,
            alerts,
        )

        return {
            "case_id": str(case.case_id),
            "summary": summary,
        }