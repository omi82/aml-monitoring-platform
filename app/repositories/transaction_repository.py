from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from app.models.transaction import Transaction


class TransactionRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):

        return (
            self.db.query(Transaction)
            .order_by(
                Transaction.transaction_timestamp.asc()
            )
            .all()
        )

    def get_by_customer(
        self,
        customer_id: str,
    ):

        return (
            self.db.query(Transaction)
            .filter(
                Transaction.customer_id == customer_id
            )
            .all()
        )

    def get_customer_with_details(
        self,
        customer_id: str,
    ):

        return (
            self.db.query(Transaction)
            .options(
                joinedload(Transaction.alerts)
            )
            .filter(
                Transaction.customer_id == customer_id
            )
            .all()
        )