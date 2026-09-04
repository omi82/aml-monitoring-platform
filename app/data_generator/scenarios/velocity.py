import random
from datetime import timedelta, datetime
from app.data_generator.utils import generate_transaction_id


class VelocityScenario:

    def inject(
        self,
        transactions,
        accounts,
        next_transaction_id,
    ):
        """
        Inject velocity transactions for a small number of customers.
        """

        suspicious_accounts = random.sample(accounts, 100)

        transaction_index = next_transaction_id

        for account in suspicious_accounts:

            # Pick one existing transaction date for this customer
            base_time = datetime.now() - timedelta(days=random.randint(0, 30))

            for minute in [0, 4, 8, 12, 16]:

                transactions.append(
                    {
                        "transaction_id": generate_transaction_id(
                            transaction_index
                        ),
                        "customer_id": account["customer_id"],
                        "account_number": account["account_number"],
                        "amount": round(
                            random.uniform(5000, 20000),
                            2,
                        ),
                        "transaction_type": "Transfer",
                        "channel": "Mobile Banking",
                        "merchant_category": "Transfer",
                        "country": "India",
                        "status": "Success",
                        "transaction_timestamp": (
                            base_time + timedelta(minutes=minute)
                        ),
                    }
                )

                transaction_index += 1

        print(
            f"Injected {(transaction_index - next_transaction_id):,} velocity transactions."
        )

        return transactions