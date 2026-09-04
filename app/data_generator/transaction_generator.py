import random
from datetime import datetime, timedelta

import pandas as pd

from app.core.constants import RAW_DATA_DIR, TRANSACTION_COUNT
from app.data_generator.export import CSVExporter
from app.data_generator.reference_data import (
    COUNTRIES,
    HIGH_RISK_COUNTRIES,
    MERCHANT_CATEGORIES,
    TRANSACTION_CHANNELS,
    TRANSACTION_CHANNEL_WEIGHTS,
    TRANSACTION_STATUS,
    TRANSACTION_STATUS_WEIGHTS,
    TRANSACTION_TYPES,
    TRANSACTION_TYPE_WEIGHTS,
)
from app.data_generator.scenarios.structuring import StructuringScenario
from app.data_generator.scenarios.velocity import VelocityScenario
from app.data_generator.utils import generate_transaction_id
from app.data_generator.scenarios.dormant_account import DormantAccountScenario


class TransactionGenerator:

    def __init__(self, customers, accounts):
        self.customers = customers
        self.accounts = accounts
        self.transactions = []

    def _generate_transaction(self, account, index):
        transaction_date = (
            datetime.now()
            - timedelta(days=random.randint(0, 365))
        )

        amount = round(
            random.uniform(100, 100000),
            2,
        )

        country = random.choices(
            population=[
                *COUNTRIES,
                *HIGH_RISK_COUNTRIES,
            ],
            weights=[
                90,
                2,
                2,
                2,
                2,
                2,
                0.5,
                0.3,
                0.2,
            ],
            k=1,
        )[0]

        return {
            "transaction_id": generate_transaction_id(index),

            "customer_id": account["customer_id"],

            "account_number": account["account_number"],

            "amount": amount,

            "transaction_type": random.choices(
                TRANSACTION_TYPES,
                weights=TRANSACTION_TYPE_WEIGHTS,
                k=1,
            )[0],

            "channel": random.choices(
                TRANSACTION_CHANNELS,
                weights=TRANSACTION_CHANNEL_WEIGHTS,
                k=1,
            )[0],

            "merchant_category": random.choice(
                MERCHANT_CATEGORIES
            ),

            "country": country,

            "status": random.choices(
                TRANSACTION_STATUS,
                weights=TRANSACTION_STATUS_WEIGHTS,
                k=1,
            )[0],

            "transaction_timestamp": transaction_date,
        }

    def generate(self):
        """
        Generate normal transactions and inject AML scenarios.
        """

        for index in range(1, TRANSACTION_COUNT + 1):

            account = random.choice(self.accounts)

            transaction = self._generate_transaction(
                account,
                index,
            )

            self.transactions.append(transaction)

        print(
            f"Generated {len(self.transactions):,} normal transactions."
        )

        self.inject_scenarios()

        print(
            f"Total transactions after scenarios: "
            f"{len(self.transactions):,}"
        )

    def inject_scenarios(self):
        """
        Inject AML scenarios into the generated dataset.
        """

        scenarios = [
            VelocityScenario(),
            StructuringScenario(),
            DormantAccountScenario(),
        ]

        for scenario in scenarios:

            self.transactions = scenario.inject(
                transactions=self.transactions,
                accounts=self.accounts,
                next_transaction_id=len(self.transactions) + 1,
            )

    def save(self):
        """
        Save generated transactions to CSV.
        """

        df = pd.DataFrame(self.transactions)

        CSVExporter.export(
            df,
            RAW_DATA_DIR / "transactions.csv",
        )