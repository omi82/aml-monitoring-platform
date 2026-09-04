from datetime import date

from pydantic import BaseModel


class AccountResponse(BaseModel):

    account_number: str

    customer_id: str

    account_type: str

    currency: str

    status: str

    opened_date: date

    model_config = {
        "from_attributes": True
    }