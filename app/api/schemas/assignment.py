from pydantic import BaseModel


class AssignCaseRequest(BaseModel):

    investigator: str