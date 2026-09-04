from pydantic import BaseModel


class AISummaryResponse(BaseModel):

    risk: str

    score: int

    confidence: int

    recommendation: str

    reasons: list[str]