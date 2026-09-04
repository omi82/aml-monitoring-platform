from datetime import timedelta

from app.aml_engine.base_rule import BaseAMLRule
from app.config.aml_rules import AML_RULES


class StructuringRule(BaseAMLRule):

    config = AML_RULES["structuring"]

    rule_name = "Structuring"

    severity = config["severity"]

    risk_score = config["risk_score"]

    threshold = config["threshold"]

    occurrences = config["occurrences"]

    time_window = timedelta(hours=config["hours"])

    def evaluate(self, context):

        alerts = []

        for customer_id, deposits in context.deposits_by_customer.items():

            qualifying = [
                txn
                for txn in deposits
                if txn.amount >= self.threshold
            ]

            if len(qualifying) < self.occurrences:
                continue

            left = 0

            for right in range(len(qualifying)):

                while (
                    qualifying[right].transaction_timestamp
                    - qualifying[left].transaction_timestamp
                    > self.time_window
                ):
                    left += 1

                window = qualifying[left:right + 1]

                if len(window) >= self.occurrences:

                    alerts.append(
                        {
                            "transaction_id": window[-1].transaction_id,
                            "rule_name": self.rule_name,
                            "severity": self.severity,
                            "risk_score": self.risk_score,
                            "status": "Open",
                            "reason": (
                                f"{len(window)} deposits of ₹{self.threshold:,}+ "
                                f"within {self.config['hours']} hours."
                            ),
                        }
                    )

                    # Only one alert per customer
                    break

        print(f"Structuring Rule: Generated {len(alerts)} alerts.")

        return alerts