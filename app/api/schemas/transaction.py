from datetime import datetime

from pydantic import BaseModel


class TransactionResponse(BaseModel):

    transaction_id: str

    account_number: str

    customer_id: str

    amount: float

    transaction_type: str

    channel: str

    merchant_category: str

    country: str

    status: str

    transaction_timestamp: datetime

    model_config = {
        "from_attributes": True
    }