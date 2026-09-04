import random
from datetime import datetime, timedelta

import pandas as pd

from app.data_generator.reference_data import (
    ACCOUNT_TYPES,
    ACCOUNT_TYPE_WEIGHTS,
    ACCOUNT_STATUS,
    ACCOUNT_STATUS_WEIGHTS,
    CURRENCIES,
)

from app.core.constants import RAW_DATA_DIR
from app.data_generator.export import CSVExporter


def generate_account_number(index: int) -> str:
    return f"ACC{index:010d}"


class AccountGenerator:

    """
    Generates synthetic bank account records
    for each customer.
    """
    def __init__(self, customers: list[dict]):
        self.customers = customers
        self.accounts = []


    def _generate_account(self, customer: dict, account_index: int):
        account_type = random.choices(
            ACCOUNT_TYPES,
            weights=ACCOUNT_TYPE_WEIGHTS,
            k=1,
        )[0]

        status = random.choices(
            ACCOUNT_STATUS,
            weights=ACCOUNT_STATUS_WEIGHTS,
            k=1,
        )[0]

        opened_date = (
            datetime.today()
            - timedelta(days=random.randint(30, 3650))
        ).date()

        return {
            "account_number": generate_account_number(account_index),
            "customer_id": customer["customer_id"],
            "account_type": account_type,
            "currency": random.choice(CURRENCIES),
            "status": status,
            "opened_date": opened_date,
        }

    def generate(self):
        """
        Generate 1-5 accounts for every customer.
        """

        account_index = 1

        for customer in self.customers:

            number_of_accounts = random.randint(1, 5)

            for account_number in range(number_of_accounts):

                account = self._generate_account(
                    customer,
                    account_index,
                )

                self.accounts.append(account)

                account_index += 1

        print(f"Generated {len(self.accounts):,} accounts.")

    def save(self):
        """
        Save generated accounts to CSV.
        """

        df = pd.DataFrame(self.accounts)

        CSVExporter.export(
            df,
            RAW_DATA_DIR / "accounts.csv",
        )