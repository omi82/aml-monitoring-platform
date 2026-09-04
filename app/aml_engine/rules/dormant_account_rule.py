from datetime import timedelta

from app.aml_engine.base_rule import BaseAMLRule
from app.config.aml_rules import AML_RULES


class DormantAccountRule(BaseAMLRule):

    config = AML_RULES["dormant_account"]

    rule_name = "Dormant Account"

    severity = config["severity"]

    risk_score = config["risk_score"]

    inactive_days = config["inactive_days"]

    threshold = config["threshold"]

    def evaluate(self, context):

        alerts = []

        inactivity_period = timedelta(days=self.inactive_days)

        for account_number, transactions in context.by_account.items():

            if len(transactions) < 2:
                continue

            for previous, current in zip(transactions, transactions[1:]):

                gap = (
                    current.transaction_timestamp
                    - previous.transaction_timestamp
                )

                if (
                    gap >= inactivity_period
                    and current.amount >= self.threshold
                ):

                    alerts.append(
                        {
                            "transaction_id": current.transaction_id,
                            "rule_name": self.rule_name,
                            "severity": self.severity,
                            "risk_score": self.risk_score,
                            "status": "Open",
                            "reason": (
                                f"Account inactive for "
                                f"{gap.days} days before a "
                                f"transaction of ₹{current.amount:,.2f}."
                            ),
                        }
                    )

                    # One alert per account
                    break

        print(
            f"Dormant Account Rule: Generated {len(alerts)} alerts."
        )

        return alerts