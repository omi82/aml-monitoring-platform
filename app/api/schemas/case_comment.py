from pydantic import BaseModel


class CaseCommentRequest(BaseModel):

    comment: str