from sqlalchemy import case, func
from sqlalchemy.orm import Session

from app.models.alert import Alert
from app.models.case import Case
from app.models.customer import Customer
from app.models.transaction import Transaction


class DashboardRepository:

    def __init__(self, db: Session):

        self.db = db

    # -----------------------------
    # KPI Cards
    # -----------------------------

    def get_total_transactions(self):

        return (
            self.db.query(
                func.count(
                    Transaction.transaction_key
                )
            )
            .scalar()
        )


    def get_total_alerts(self):

        return (
            self.db.query(
                func.count(Alert.alert_key)
            )
            .scalar()
        )


    def get_open_alerts(self):

        return (
            self.db.query(
                func.count(Alert.alert_key)
            )
            .filter(
                Alert.status == "Open"
            )
            .scalar()
        )


    def get_total_cases(self):

        return (
            self.db.query(
                func.count(Case.case_id)
            )
            .scalar()
        )


    def get_open_cases(self):

        return (
            self.db.query(
                func.count(Case.case_id)
            )
            .filter(
                Case.status == "Open"
            )
            .scalar()
        )


    def get_critical_cases(self):

        return (
            self.db.query(
                func.count(Case.case_id)
            )
            .filter(
                Case.priority == "Critical"
            )
            .scalar()
        )


    def get_total_customers(self):

        return (
            self.db.query(
                func.count(Customer.customer_key)
            )
            .scalar()
        )


    def get_average_risk(self):

        risk_score = case(
            (Customer.risk_category == "LOW", 1),
            (Customer.risk_category == "MEDIUM", 2),
            (Customer.risk_category == "HIGH", 3),
            else_=0,
        )

        average = (
            self.db.query(
                func.avg(risk_score)
            )
            .scalar()
        )

        if average is None:
            return 0

        return round(
            float(average),
            2,
        )

    # -----------------------------
    # Dashboard Tables
    # -----------------------------

    def get_recent_alerts(self, limit=10):

        return (
            self.db.query(Alert)
            .order_by(Alert.alert_key.desc())
            .limit(limit)
            .all()
        )

    def get_recent_cases(self, limit=10):

        return (
            self.db.query(Case)
            .order_by(Case.created_at.desc())
            .limit(limit)
            .all()
        )

    # -----------------------------
    # Dashboard Charts
    # -----------------------------

    def get_alerts_by_severity(self):

        return (
            self.db.query(
                Alert.severity,
                func.count(Alert.alert_key).label("count"),
            )
            .group_by(Alert.severity)
            .all()
        )

    def get_alerts_by_rule(self):

        return (
            self.db.query(
                Alert.rule_name,
                func.count(Alert.alert_key).label("count"),
            )
            .group_by(Alert.rule_name)
            .order_by(func.count(Alert.alert_key).desc())
            .all()
        )

    def get_risk_distribution(self):

        return (
            self.db.query(
                Customer.risk_category,
                func.count(Customer.customer_key).label("count"),
            )
            .group_by(Customer.risk_category)
            .all()
        )