import random
from datetime import timedelta

from app.data_generator.reference_data import (
    MERCHANT_CATEGORIES,
    TRANSACTION_CHANNELS,
    TRANSACTION_STATUS,
)
from app.data_generator.utils import generate_transaction_id


class StructuringScenario:
    """
    Inject Structuring (Smurfing) transactions.

    Multiple deposits just below the reporting threshold
    within a short time period.
    """

    def inject(
        self,
        transactions,
        accounts,
        next_transaction_id,
    ):
        suspicious_accounts = random.sample(accounts, 50)

        transaction_index = next_transaction_id

        injected_count = 0

        for account in suspicious_accounts:

            # Random base time
            base_time = random.choice(transactions)[
                "transaction_timestamp"
            ]

            for _ in range(5):

                transaction = {
                    "transaction_id": generate_transaction_id(
                        transaction_index
                    ),

                    "customer_id": account["customer_id"],

                    "account_number": account["account_number"],

                    # Just below reporting threshold
                    "amount": round(
                        random.uniform(90000, 99999),
                        2,
                    ),

                    # Deposits are most common for structuring
                    "transaction_type": "Deposit",

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

                    # Within 24 hours
                    "transaction_timestamp": (
                        base_time
                        + timedelta(
                            minutes=random.randint(0, 24 * 60)
                        )
                    ),
                }

                transactions.append(transaction)

                transaction_index += 1

                injected_count += 1

        print(
            f"Injected {injected_count:,} structuring transactions."
        )

        return transactions