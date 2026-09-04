from app.aml_engine.base_rule import BaseAMLRule
from app.config.aml_rules import AML_RULES


class HighRiskCountryRule(BaseAMLRule):

    config = AML_RULES["high_risk_country"]

    rule_name = "High Risk Country"

    severity = config["severity"]

    risk_score = config["risk_score"]

    def __init__(self, high_risk_countries):

        self.high_risk_countries = high_risk_countries

    def evaluate(self, context):

        alerts = []

        for transaction in context.transactions:

            if transaction.country not in self.high_risk_countries:
                continue

            alerts.append(
                {
                    "transaction_id": transaction.transaction_id,
                    "rule_name": self.rule_name,
                    "severity": self.severity,
                    "risk_score": self.risk_score,
                    "status": "Open",
                    "reason": (
                        f"Transaction originated from "
                        f"high-risk country: {transaction.country}"
                    ),
                }
            )

        return alerts