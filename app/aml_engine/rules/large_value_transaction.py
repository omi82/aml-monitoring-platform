from app.aml_engine.base_rule import BaseAMLRule
from app.config.aml_rules import AML_RULES


class LargeValueTransactionRule(BaseAMLRule):

    config = AML_RULES["large_value_transaction"]

    rule_name = "Large Value Transaction"

    threshold = config["threshold"]

    severity = config["severity"]

    risk_score = config["risk_score"]

    def evaluate(self, context):

        alerts = []

        for transaction in context.transactions:

            if transaction.amount < self.threshold:
                continue

            alerts.append(
                {
                    "transaction_id": transaction.transaction_id,
                    "rule_name": self.rule_name,
                    "severity": self.severity,
                    "risk_score": self.risk_score,
                    "status": "Open",
                    "reason": (
                        f"Transaction amount "
                        f"{transaction.amount} exceeds "
                        f"{self.threshold}"
                    ),
                }
            )

        return alerts