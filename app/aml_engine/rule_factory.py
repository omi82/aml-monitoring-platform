from app.aml_engine.rules.large_value_transaction import LargeValueTransactionRule
from app.aml_engine.rules.high_risk_country import HighRiskCountryRule
from app.repositories.country_repository import CountryRepository
from app.aml_engine.rules.velocity_rule import VelocityRule
from app.aml_engine.rules.structuring_rule import StructuringRule
from app.aml_engine.rules.dormant_account_rule import DormantAccountRule


class AMLRuleFactory:

    @staticmethod
    def create_rules(db):

        country_repo = CountryRepository(db)

        high_risk_countries = country_repo.get_high_risk_countries()

        return [
            LargeValueTransactionRule(),
            HighRiskCountryRule(high_risk_countries),
            VelocityRule(),
            StructuringRule(),
            DormantAccountRule(),
        ]