from pydantic import BaseModel


class PageFilter(BaseModel):

    page: int = 1
    size: int = 20