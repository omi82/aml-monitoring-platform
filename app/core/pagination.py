from math import ceil


def build_pagination(
    total_records: int,
    page: int,
    size: int,
):

    return {
        "page": page,
        "size": size,
        "total_records": total_records,
        "total_pages": ceil(total_records / size)
        if total_records > 0
        else 0,
    }