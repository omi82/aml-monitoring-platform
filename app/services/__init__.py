from app.repositories.customer_repository import CustomerRepository
from app.repositories.transaction_repository import TransactionRepository
from app.repositories.case_repository import CaseRepository
from app.repositories.timeline_repository import TimelineRepository

def __init__(self, db):

    self.customer_repo = CustomerRepository(db)

    self.transaction_repo = TransactionRepository(db)

    self.case_repo = CaseRepository(db)

    self.timeline_repo = TimelineRepository(db)