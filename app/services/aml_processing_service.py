import time

from app.aml_engine.engine import AMLRuleEngine
from app.repositories.alert_repository import AlertRepository
from app.repositories.transaction_repository import TransactionRepository
from app.services.case_creation_service import CaseCreationService
from app.utils.logger import get_logger

logger = get_logger(__name__)


class AMLProcessingService:
    """
    Service responsible for executing the AML detection pipeline.
    """

    def __init__(self, db):

        self.db = db

        self.transaction_repo = TransactionRepository(db)
        self.alert_repo = AlertRepository(db)

        self.engine = AMLRuleEngine(db)

        self.case_creation_service = CaseCreationService(db)

    def process(self):

        start_time = time.perf_counter()

        logger.info("=" * 60)
        logger.info("AML ENGINE STARTED")
        logger.info("=" * 60)

        logger.info("Loading transactions...")

        transactions = self.transaction_repo.get_all()

        logger.info(
            "Loaded %s transactions.",
            f"{len(transactions):,}",
        )

        logger.info(
            "Registered AML Rules : %d",
            len(self.engine.rules),
        )

        # Execute AML Rules
        all_alerts = self.engine.evaluate_transactions(transactions)

        generated = len(all_alerts)

        logger.info(
            "Generated %s alerts.",
            f"{generated:,}",
        )

        # Save Alerts
        saved = self.alert_repo.bulk_create(all_alerts)

        logger.info(
            "Saved %s alerts.",
            f"{saved:,}",
        )

        # Automatically Create Investigation Cases
        created_cases = (
            self.case_creation_service.create_cases_for_new_alerts()
        )

        logger.info(
            "Created %s investigation cases.",
            f"{created_cases:,}",
        )

        elapsed = time.perf_counter() - start_time

        logger.info(
            "Execution Time : %.2f seconds",
            elapsed,
        )

        logger.info("=" * 60)
        logger.info("AML ENGINE COMPLETED")
        logger.info("=" * 60)

        return {
            "transactions": len(transactions),
            "generated_alerts": generated,
            "saved_alerts": saved,
            "created_cases": created_cases,
            "execution_time": elapsed,
            "rules": len(self.engine.rules),
        }