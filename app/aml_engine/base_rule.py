from abc import ABC, abstractmethod


class BaseAMLRule(ABC):
    """
    Base class for all AML rules.
    """

    rule_name: str = ""
    severity: str = "Medium"

    @abstractmethod
    def evaluate(self, transaction: dict):
        """
        Evaluate a transaction.

        Returns:
            dict | None
        """
        pass