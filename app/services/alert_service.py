from app.repositories.alert_repository import AlertRepository
from math import ceil
from app.core.pagination import build_pagination



class AlertService:

    def __init__(self, db):

        self.repository = AlertRepository(db)


    def get_all_alerts(
        self,
        filters,
    ):
        return self.repository.get_all(filters)

    def get_open_alerts(self):

        return self.repository.get_open_alerts()