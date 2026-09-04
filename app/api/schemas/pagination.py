from math import ceil

from pydantic import BaseModel


class PaginationMeta(BaseModel):

    page: int
    size: int
    total_records: int
    total_pages: int


class PaginatedResponse(BaseModel):

    data: list
    pagination: PaginationMeta