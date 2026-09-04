from sqlalchemy import asc, desc
from sqlalchemy.dialects.postgresql import insert

from app.models.alert import Alert
from app.repositories.base_repository import BaseRepository


class AlertRepository(BaseRepository):

    def __init__(self, db):
        super().__init__(db, Alert)

    def bulk_create(self, alerts_data):

        if not alerts_data:
            return 0

        batch_size = 5000
        inserted_total = 0

        for i in range(0, len(alerts_data), batch_size):

            batch = alerts_data[i:i + batch_size]

            stmt = (
                insert(Alert)
                .values(batch)
                .on_conflict_do_nothing(
                    index_elements=[
                        "transaction_id",
                        "rule_name",
                    ]
                )
                .returning(Alert.alert_key)
            )

            result = self.db.execute(stmt)

            inserted_total += len(result.fetchall())

            self.db.commit()

        return inserted_total

    def save_alerts(self, alerts_data):

        return self.bulk_create(alerts_data)

    def get_open_alerts(self):

        return (
            self.db.query(Alert)
            .filter(
                Alert.status == "Open"
            )
            .all()
        )

    def get_by_alert_key(
        self,
        alert_key: int,
    ):

        return (
            self.db.query(Alert)
            .filter(
                Alert.alert_key == alert_key
            )
            .first()
        )

    def get_all(
        self,
        filters,
    ):

        query = self.db.query(Alert)

        if filters.status:
            query = query.filter(
                Alert.status == filters.status
            )

        if filters.severity:
            query = query.filter(
                Alert.severity == filters.severity
            )

        if filters.rule_name:
            query = query.filter(
                Alert.rule_name == filters.rule_name
            )

        if filters.min_risk_score is not None:
            query = query.filter(
                Alert.risk_score >= filters.min_risk_score
            )

        if filters.max_risk_score is not None:
            query = query.filter(
                Alert.risk_score <= filters.max_risk_score
            )

        sort_column = getattr(
            Alert,
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

        offset = (
            filters.page - 1
        ) * filters.size

        return (
            query
            .offset(offset)
            .limit(filters.size)
            .all()
        )

    def get_by_case(
        self,
        case_id,
    ):

        return (
            self.db.query(Alert)
            .filter(
                Alert.case_id == case_id
            )
            .all()
        )