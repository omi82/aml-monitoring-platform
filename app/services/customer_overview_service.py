from app.repositories.customer_repository import CustomerRepository
from app.repositories.account_repository import AccountRepository
from app.repositories.transaction_repository import TransactionRepository
from app.repositories.alert_repository import AlertRepository
from app.repositories.case_repository import CaseRepository
from app.repositories.timeline_repository import TimelineRepository

from app.ai.investigation_engine import InvestigationEngine


class CustomerOverviewService:

    def __init__(self, db):

        self.customer_repo = CustomerRepository(db)

        self.account_repo = AccountRepository(db)

        self.transaction_repo = TransactionRepository(db)

        self.alert_repo = AlertRepository(db)

        self.case_repo = CaseRepository(db)

        self.timeline_repo = TimelineRepository(db)


    def get_overview(
        self,
        customer_id: str,
    ):

        # ==================================================
        # CUSTOMER
        # ==================================================

        customer = self.customer_repo.get_by_id(
            customer_id
        )

        if customer is None:

            return None


        # ==================================================
        # ACCOUNTS
        # ==================================================

        accounts = self.account_repo.get_by_customer(
            customer_id
        )


        # ==================================================
        # TRANSACTIONS
        # ==================================================

        transactions = (
            self.transaction_repo.get_customer_with_details(
                customer_id
            )
        )


        # ==================================================
        # ALERTS
        # ==================================================

        alerts = []

        for transaction in transactions:

            alerts.extend(
                transaction.alerts
            )


        # ==================================================
        # ALERT KEYS
        # ==================================================

        alert_keys = [
            alert.alert_key
            for alert in alerts
        ]


        # ==================================================
        # CASES LINKED TO ALERTS
        # ==================================================

        alert_cases = (
            self.case_repo.get_by_alert_keys(
                alert_keys
            )
        )


        # ==================================================
        # CASES CREATED DIRECTLY FOR CUSTOMER
        # ==================================================

        customer_cases = (
            self.case_repo.get_by_customer(
                customer_id
            )
        )


        # ==================================================
        # COMBINE CASES
        # ==================================================

        cases_by_id = {}

        for case in alert_cases:

            cases_by_id[
                case.case_id
            ] = case


        for case in customer_cases:

            cases_by_id[
                case.case_id
            ] = case


        cases = list(
            cases_by_id.values()
        )


        # ==================================================
        # TIMELINE
        # ==================================================

        case_ids = [
            case.case_id
            for case in cases
        ]


        timeline = (
            self.timeline_repo.get_by_case_ids(
                case_ids
            )
        )


        # ==================================================
        # AI SUMMARY
        # ==================================================

        ai_summary = InvestigationEngine.analyze(

            customer,

            transactions,

            alerts,

            cases,

        )


        # ==================================================
        # RESPONSE
        # ==================================================

        return {

            "customer": customer,

            "accounts": accounts,

            "transactions": transactions,

            "alerts": alerts,

            "cases": cases,

            "timeline": timeline,

            "ai_summary": ai_summary,

        }