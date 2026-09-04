from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.api.schemas.ai_chat import (
    AIChatRequest,
    AIChatResponse,
)

from app.repositories.customer_repository import CustomerRepository
from app.repositories.account_repository import AccountRepository
from app.repositories.transaction_repository import TransactionRepository
from app.repositories.case_repository import CaseRepository
from app.repositories.timeline_repository import TimelineRepository

from app.ai.chat_engine import ChatEngine


router = APIRouter(
    prefix="/ai",
    tags=["AI"],
)


@router.post(
    "/chat",
    response_model=AIChatResponse,
)
def chat(
    request: AIChatRequest,
    db: Session = Depends(get_db),
):

    # ==================================================
    # REPOSITORIES
    # ==================================================

    customer_repo = CustomerRepository(db)

    account_repo = AccountRepository(db)

    transaction_repo = TransactionRepository(db)

    case_repo = CaseRepository(db)

    timeline_repo = TimelineRepository(db)


    # ==================================================
    # CUSTOMER
    # ==================================================

    customer = customer_repo.get_by_id(
        request.customer_id
    )

    if customer is None:

        raise HTTPException(
            status_code=404,
            detail="Customer not found.",
        )


    # ==================================================
    # ACCOUNTS
    # ==================================================

    accounts = account_repo.get_by_customer(
        request.customer_id
    )


    # ==================================================
    # TRANSACTIONS
    # ==================================================

    transactions = (
        transaction_repo.get_customer_with_details(
            request.customer_id
        )
    )


    # ==================================================
    # ALERTS
    # ==================================================

    alerts = []

    for transaction in transactions:

        alerts.extend(
            transaction.alerts
        )


    # ==================================================
    # ALERT KEYS
    # ==================================================

    alert_keys = [
        alert.alert_key
        for alert in alerts
    ]


    # ==================================================
    # CASES LINKED TO ALERTS
    # ==================================================

    alert_cases = (
        case_repo.get_by_alert_keys(
            alert_keys
        )
    )


    # ==================================================
    # CASES CREATED DIRECTLY FOR CUSTOMER
    # ==================================================

    customer_cases = (
        case_repo.get_by_customer(
            request.customer_id
        )
    )


    # ==================================================
    # COMBINE CASES
    # ==================================================

    cases_by_id = {}


    for case in alert_cases:

        cases_by_id[
            case.case_id
        ] = case


    for case in customer_cases:

        cases_by_id[
            case.case_id
        ] = case


    cases = list(
        cases_by_id.values()
    )


    # ==================================================
    # TIMELINE
    # ==================================================

    case_ids = [
        case.case_id
        for case in cases
    ]


    timeline = (
        timeline_repo.get_by_case_ids(
            case_ids
        )
    )


    # ==================================================
    # AI CHAT ENGINE
    # ==================================================

    chat_engine = ChatEngine()


    answer = chat_engine.answer(

        question=request.question,

        conversation=request.conversation,

        customer=customer,

        accounts=accounts,

        alerts=alerts,

        transactions=transactions,

        cases=cases,

        timeline=timeline,

    )


    # ==================================================
    # STRUCTURED AI RESPONSE
    # ==================================================

    return AIChatResponse(

        risk_assessment=answer[
            "risk_assessment"
        ],

        key_findings=answer[
            "key_findings"
        ],

        recommendations=answer[
            "recommendations"
        ],

        conclusion=answer[
            "conclusion"
        ],

    )