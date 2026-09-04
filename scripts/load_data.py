import pandas as pd

from app.core.constants import PROCESSED_DATA_DIR
from app.database.session import SessionLocal
from app.loaders.base_loader import BaseLoader

from app.models.account import Account
from app.models.customer import Customer
from app.models.transaction import Transaction


def main():

    db = SessionLocal()

    loader = BaseLoader(db)

    try:

        from app.core.constants import (
            PROCESSED_ACCOUNTS_FILE,
            PROCESSED_CUSTOMERS_FILE,
            PROCESSED_TRANSACTIONS_FILE,
        )

        datasets = [
            (Customer, PROCESSED_CUSTOMERS_FILE),
            (Account, PROCESSED_ACCOUNTS_FILE),
            (Transaction, PROCESSED_TRANSACTIONS_FILE),
        ]

        for model, file_path in datasets:

            print(f"\nLoading {file_path.name}")

            dataframe = pd.read_csv(file_path)

            loader.load_dataframe(
                model,
                dataframe,
            )

        print(
            "\nData Warehouse Loaded Successfully."
        )

    finally:

        db.close()


if __name__ == "__main__":
    main()