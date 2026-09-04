ALLOWED_TRANSITIONS = {

    "Open": [
        "Assigned",
    ],

    "Assigned": [
        "Investigating",
    ],

    "Investigating": [
        "Waiting Documents",
        "Escalated",
        "False Positive",
        "Closed",
    ],

    "Waiting Documents": [
        "Investigating",
        "Closed",
    ],

    "Escalated": [
        "Investigating",
        "Closed",
    ],

    "False Positive": [],

    "Closed": [],
}


def is_valid_transition(
    current_status: str,
    new_status: str,
) -> bool:

    allowed = ALLOWED_TRANSITIONS.get(
        current_status,
        [],
    )

    return new_status in allowed