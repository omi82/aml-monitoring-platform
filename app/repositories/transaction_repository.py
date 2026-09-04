from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.transaction import Transaction


class TransactionRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.scalars(
            select(Transaction)
        ).all()