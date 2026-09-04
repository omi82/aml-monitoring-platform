def apply_filters(
    query,
    filters: dict,
):

    for column, value in filters.items():

        if value is not None:
            query = query.filter(column == value)

    return query