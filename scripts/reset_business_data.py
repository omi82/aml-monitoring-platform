from app.database.session import SessionLocal

from app.models.case_timeline import CaseTimeline
from app.models.case import Case
from app.models.alert import Alert
from app.models.transaction import Transaction
from app.models.account import Account
from app.models.customer import Customer


def main():

    db = SessionLocal()

    try:

        print("Resetting business data...")

        # Delete investigation timeline
        timeline_count = (
            db.query(CaseTimeline).delete(
                synchronize_session=False
            )
        )

        print(
            f"Deleted {timeline_count:,} timeline records."
        )

        # Delete cases
        case_count = (
            db.query(Case).delete(
                synchronize_session=False
            )
        )

        print(
            f"Deleted {case_count:,} case records."
        )

        # Delete alerts
        alert_count = (
            db.query(Alert).delete(
                synchronize_session=False
            )
        )

        print(
            f"Deleted {alert_count:,} alert records."
        )

        # Delete transactions
        transaction_count = (
            db.query(Transaction).delete(
                synchronize_session=False
            )
        )

        print(
            f"Deleted {transaction_count:,} transaction records."
        )

        # Delete accounts
        account_count = (
            db.query(Account).delete(
                synchronize_session=False
            )
        )

        print(
            f"Deleted {account_count:,} account records."
        )

        # Delete customers
        customer_count = (
            db.query(Customer).delete(
                synchronize_session=False
            )
        )

        print(
            f"Deleted {customer_count:,} customer records."
        )

        db.commit()

        print()
        print("Business data reset successfully.")

    except Exception:

        db.rollback()

        raise

    finally:

        db.close()


if __name__ == "__main__":
    main()