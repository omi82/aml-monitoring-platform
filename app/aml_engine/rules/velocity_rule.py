from datetime import timedelta

from app.aml_engine.base_rule import BaseAMLRule
from app.config.aml_rules import AML_RULES
from app.utils.logger import get_logger

logger = get_logger(__name__)


class VelocityRule(BaseAMLRule):

    config = AML_RULES["velocity"]

    rule_name = "Velocity Detection"

    severity = config["severity"]

    risk_score = config["risk_score"]

    transaction_count = config["transaction_count"]

    time_window = timedelta(
        minutes=config["time_window_minutes"]
    )

    def evaluate(self, context):

        alerts = []

        for customer_id, transactions in context.by_customer.items():

            left = 0

            for right in range(len(transactions)):

                while (
                    transactions[right].transaction_timestamp
                    - transactions[left].transaction_timestamp
                ) > self.time_window:
                    left += 1

                window_size = right - left + 1

                if window_size >= self.transaction_count:

                    alerts.append(
                        {
                            "transaction_id": transactions[right].transaction_id,
                            "rule_name": self.rule_name,
                            "severity": self.severity,
                            "risk_score": self.risk_score,
                            "status": "Open",
                            "reason": (
                                f"{window_size} transactions "
                                f"within "
                                f"{self.config['time_window_minutes']} minutes "
                                f"for customer {customer_id}"
                            ),
                        }
                    )

        logger.info(
            "Velocity Rule: Generated %s alerts.",
            f"{len(alerts):,}",
        )

        return alerts