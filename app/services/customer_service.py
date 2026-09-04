from app.repositories.customer_repository import CustomerRepository


class CustomerService:

    def __init__(self, db):

        self.repository = CustomerRepository(db)

    def get_all_customers(
        self,
        filters,
    ):
        return self.repository.get_all(filters)

    def get_customer_by_id(self, customer_id):

        return self.repository.get_by_id(customer_id)