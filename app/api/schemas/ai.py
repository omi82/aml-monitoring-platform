from pydantic import BaseModel


class AISummaryResponse(BaseModel):
    case_id: str
    summary: str