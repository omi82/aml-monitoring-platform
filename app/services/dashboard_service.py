from app.repositories.dashboard_repository import DashboardRepository


class DashboardService:

    def __init__(self, db):

        self.repository = DashboardRepository(db)

    def get_summary(self):

        return {
            "total_transactions": self.repository.get_total_transactions(),
            "total_alerts": self.repository.get_total_alerts(),
            "open_alerts": self.repository.get_open_alerts(),
            "total_cases": self.repository.get_total_cases(),
            "open_cases": self.repository.get_open_cases(),
            "critical_cases": self.repository.get_critical_cases(),
        }

    def get_recent_alerts(self):

        return self.repository.get_recent_alerts()

    def get_recent_cases(self):

        return self.repository.get_recent_cases()

    def get_alerts_by_severity(self):

        return self.repository.get_alerts_by_severity()

    def get_alerts_by_rule(self):

        return self.repository.get_alerts_by_rule()

    def get_risk_distribution(self):

        return self.repository.get_risk_distribution()