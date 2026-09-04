import random
from datetime import timedelta

from app.data_generator.reference_data import (
    MERCHANT_CATEGORIES,
    TRANSACTION_CHANNELS,
    TRANSACTION_STATUS,
)
from app.data_generator.utils import generate_transaction_id


class DormantAccountScenario:
    """
    Inject dormant account activity.

    A dormant account becomes active after
    180+ days with a large transaction.
    """

    def inject(
        self,
        transactions,
        accounts,
        next_transaction_id,
    ):

        suspicious_accounts = random.sample(accounts, 100)

        transaction_index = next_transaction_id

        injected = 0

        for account in suspicious_accounts:

            customer_transactions = [
                txn
                for txn in transactions
                if txn["account_number"] == account["account_number"]
            ]

            if not customer_transactions:
                continue

            last_transaction = max(
                customer_transactions,
                key=lambda t: t["transaction_timestamp"]
            )

            dormant_transaction = {

                "transaction_id": generate_transaction_id(
                    transaction_index
                ),

                "customer_id": account["customer_id"],

                "account_number": account["account_number"],

                "amount": round(
                    random.uniform(500000, 1000000),
                    2,
                ),

                "transaction_type": random.choice(
                    [
                        "Deposit",
                        "Withdrawal",
                    ]
                ),

                "channel": random.choice(
                    TRANSACTION_CHANNELS
                ),

                "merchant_category": random.choice(
                    MERCHANT_CATEGORIES
                ),

                "country": "India",

                "status": random.choice(
                    TRANSACTION_STATUS
                ),

                "transaction_timestamp": (
                    last_transaction["transaction_timestamp"]
                    + timedelta(
                        days=random.randint(181, 365)
                    )
                ),
            }

            transactions.append(dormant_transaction)

            transaction_index += 1

            injected += 1

        print(
            f"Injected {injected} dormant account transactions."
        )

        return transactions