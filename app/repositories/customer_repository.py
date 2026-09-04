from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

from app.models.customer import Customer


class CustomerRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(
        self,
        filters,
    ):

        query = self.db.query(Customer)

        if filters.country:
            query = query.filter(
                Customer.country == filters.country
            )

        if filters.risk_level:
            query = query.filter(
                Customer.risk_level == filters.risk_level
            )

        if filters.customer_type:
            query = query.filter(
                Customer.customer_type == filters.customer_type
            )

        total = query.count()

        sort_column = getattr(
            Customer,
            filters.sort_by,
        )

        if filters.sort_order == "asc":

            query = query.order_by(
                asc(sort_column)
            )

        else:

            query = query.order_by(
                desc(sort_column)
            )

        customers = (
            query
            .offset(
                (filters.page - 1) * filters.size
            )
            .limit(filters.size)
            .all()
        )

        return {
            "items": customers,
            "total": total,
            "page": filters.page,
            "size": filters.size,
        }

    def get_by_id(
        self,
        customer_id,
    ):

        return (
            self.db.query(Customer)
            .filter(
                Customer.customer_id == customer_id
            )
            .first()
        )

    def get_by_id(self, customer_id):

        return (
            self.db.query(Customer)
            .filter(Customer.customer_id == customer_id)
            .first()
        )