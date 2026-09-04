from app.aml_engine.context import AMLContext
from app.aml_engine.rule_factory import AMLRuleFactory


class AMLRuleEngine:
    """
    Execute all registered AML rules.
    """

    def __init__(self, db):

        self.rules = AMLRuleFactory.create_rules(db)

    def evaluate_transactions(self, transactions):

        context = AMLContext(transactions)

        all_alerts = []

        for rule in self.rules:

            alerts = rule.evaluate(context)

            if alerts:
                all_alerts.extend(alerts)

        return all_alerts