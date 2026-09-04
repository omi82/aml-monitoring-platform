from app.aml_engine.rules.large_value_transaction import LargeValueTransactionRule
from app.aml_engine.rules.high_risk_country import HighRiskCountryRule

RULES = [
    LargeValueTransactionRule,
    HighRiskCountryRule,
]