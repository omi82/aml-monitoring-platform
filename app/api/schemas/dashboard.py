from pydantic import BaseModel


class DashboardSummaryResponse(BaseModel):

    total_transactions: int
    total_alerts: int
    open_alerts: int
    total_cases: int
    open_cases: int
    critical_cases: int


class ChartResponse(BaseModel):

    label: str
    count: int