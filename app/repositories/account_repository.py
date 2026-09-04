from sqlalchemy.orm import Session

from app.models.account import Account


class AccountRepository:

    def __init__(self, db: Session):

        self.db = db

    def get_by_customer(
        self,
        customer_id: str,
    ):

        return (
            self.db.query(Account)
            .filter(Account.customer_id == customer_id)
            .all()
        )

    def get_by_account_number(
        self,
        account_number: str,
    ):

        return (
            self.db.query(Account)
            .filter(Account.account_number == account_number)
            .first()
        )