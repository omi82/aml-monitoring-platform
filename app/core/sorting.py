from sqlalchemy import asc, desc


def apply_sorting(
    query,
    model,
    sort_by,
    sort_order,
):

    if not sort_by:
        return query

    if not hasattr(model, sort_by):
        return query

    column = getattr(model, sort_by)

    if sort_order.lower() == "asc":
        return query.order_by(asc(column))

    return query.order_by(desc(column))