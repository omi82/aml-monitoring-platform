from pydantic import BaseModel


class CustomerResponse(BaseModel):

    customer_id: str
    full_name: str
    gender: str
    age: int
    occupation: str
    annual_income: float
    kyc_status: bool
    risk_category: str

    model_config = {
        "from_attributes": True,
    }


class CustomerListResponse(BaseModel):

    items: list[CustomerResponse]

    total: int

    page: int

    size: int