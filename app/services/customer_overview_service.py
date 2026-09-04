from app.repositories.customer_repository import CustomerRepository
from app.repositories.alert_repository import AlertRepository
from app.repositories.case_repository import CaseRepository
from app.repositories.timeline_repository import TimelineRepository


class CustomerOverviewService:

    def __init__(self, db):

        self.customer_repo = CustomerRepository(db)
        self.alert_repo = AlertRepository(db)
        self.case_repo = CaseRepository(db)
        self.timeline_repo = TimelineRepository(db)

    def get_overview(
        self,
        customer_id,
    ):

        customer = self.customer_repo.get_by_id(customer_id)

        alerts = self.alert_repo.get_by_customer(customer_id)

        cases = self.case_repo.get_by_customer(customer_id)

        timeline = self.timeline_repo.get_by_customer(customer_id)

        return {

            "customer": customer,

            "alerts": alerts,

            "cases": cases,

            "timeline": timeline,

        }