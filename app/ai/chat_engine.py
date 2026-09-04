from json import loads

from app.ai.engine_llm import EngineLLM
from app.ai.prompt_builder import PromptBuilder


class ChatEngine:

    def __init__(self):

        self.llm = EngineLLM()


    def answer(
        self,
        question,
        conversation,
        customer,
        accounts,
        alerts,
        transactions,
        cases,
        timeline,
    ):

        question_lower = question.lower().strip()


        # ==================================================
        # DETERMINISTIC FACTUAL QUESTIONS
        # ==================================================

        # ------------------------------------------
        # Account count
        # ------------------------------------------

        if (
            "how many account" in question_lower
            or "number of account" in question_lower
        ):

            count = len(accounts)

            return {
                "risk_assessment":
                    customer.risk_category,

                "key_findings": [
                    f"Customer has {count} account(s) "
                    "according to the account records."
                ],

                "recommendations": [],

                "conclusion":
                    f"Customer {customer.full_name} "
                    f"has {count} account(s).",
            }


        # ------------------------------------------
        # Alert count
        # ------------------------------------------

        if (
            "how many alert" in question_lower
            or "number of alert" in question_lower
        ):

            count = len(alerts)

            return {
                "risk_assessment":
                    customer.risk_category,

                "key_findings": [
                    f"Customer has {count} alert(s) "
                    "according to the alert records."
                ],

                "recommendations": [],

                "conclusion":
                    f"Customer has {count} alert(s).",
            }


        # ------------------------------------------
        # Case count
        # ------------------------------------------

        if (
            "how many case" in question_lower
            or "number of case" in question_lower
        ):

            count = len(cases)

            return {
                "risk_assessment":
                    customer.risk_category,

                "key_findings": [
                    f"Customer has {count} case(s) "
                    "according to the case records."
                ],

                "recommendations": [],

                "conclusion":
                    f"Customer has {count} case(s).",
            }


        # ------------------------------------------
        # Last transaction
        # ------------------------------------------

        if (
            "last transaction" in question_lower
            or "latest transaction" in question_lower
        ):

            if not transactions:

                return {
                    "risk_assessment":
                        customer.risk_category,

                    "key_findings": [
                        "No transaction records are "
                        "available for this customer."
                    ],

                    "recommendations": [],

                    "conclusion":
                        "The last transaction cannot "
                        "be determined because no "
                        "transaction records are available.",
                }


            latest_transaction = max(
                transactions,
                key=lambda transaction:
                    transaction.transaction_timestamp
            )


            # Account question

            if (
                "which account" in question_lower
                or "what account" in question_lower
                or "account number" in question_lower
            ):

                return {

                    "risk_assessment":
                        customer.risk_category,

                    "key_findings": [
                        "The latest transaction "
                        f"is {latest_transaction.transaction_id}.",

                        "The transaction is associated "
                        f"with account "
                        f"{latest_transaction.account_number}.",
                    ],

                    "recommendations": [],

                    "conclusion":
                        "The latest transaction was "
                        f"associated with account "
                        f"{latest_transaction.account_number}.",
                }


            # Date question

            if (
                "date" in question_lower
                or "when" in question_lower
            ):

                return {

                    "risk_assessment":
                        customer.risk_category,

                    "key_findings": [
                        "The latest transaction is "
                        f"{latest_transaction.transaction_id}.",

                        "Its transaction timestamp is "
                        f"{latest_transaction.transaction_timestamp}.",
                    ],

                    "recommendations": [],

                    "conclusion":
                        "The latest transaction occurred "
                        f"on "
                        f"{latest_transaction.transaction_timestamp}.",
                }


            # Generic last transaction

            return {

                "risk_assessment":
                    customer.risk_category,

                "key_findings": [

                    f"Transaction ID: "
                    f"{latest_transaction.transaction_id}",

                    f"Account: "
                    f"{latest_transaction.account_number}",

                    f"Amount: "
                    f"{latest_transaction.amount}",

                    f"Type: "
                    f"{latest_transaction.transaction_type}",

                    f"Channel: "
                    f"{latest_transaction.channel}",

                    f"Timestamp: "
                    f"{latest_transaction.transaction_timestamp}",
                ],

                "recommendations": [],

                "conclusion":
                    "The latest transaction is "
                    f"{latest_transaction.transaction_id} "
                    f"on account "
                    f"{latest_transaction.account_number}.",
            }


        # ==================================================
        # LATEST TIMELINE ACTION
        # ==================================================

        if (
            "last investigation action"
            in question_lower
            or "latest investigation action"
            in question_lower
            or "last timeline" in question_lower
            or "latest timeline" in question_lower
        ):

            if not timeline:

                return {

                    "risk_assessment":
                        customer.risk_category,

                    "key_findings": [
                        "No timeline records are "
                        "available for this customer."
                    ],

                    "recommendations": [],

                    "conclusion":
                        "The latest investigation action "
                        "cannot be determined because "
                        "no timeline records are available.",
                }


            latest_event = max(
                timeline,
                key=lambda event:
                    event.created_at
            )


            return {

                "risk_assessment":
                    customer.risk_category,

                "key_findings": [

                    f"Action: "
                    f"{latest_event.action}",

                    f"Performed by: "
                    f"{latest_event.performed_by}",

                    f"Created at: "
                    f"{latest_event.created_at}",

                ],

                "recommendations": [],

                "conclusion":
                    "The latest investigation action was "
                    f"'{latest_event.action}' performed by "
                    f"{latest_event.performed_by}.",
            }


        # ==================================================
        # LATEST CASE
        # ==================================================

        if (
            "latest case" in question_lower
            or "last case" in question_lower
        ):

            if not cases:

                return {

                    "risk_assessment":
                        customer.risk_category,

                    "key_findings": [
                        "No case records are "
                        "available for this customer."
                    ],

                    "recommendations": [],

                    "conclusion":
                        "There is no case available "
                        "for this customer.",
                }


            latest_case = max(
                cases,
                key=lambda case:
                    case.created_at
            )


            return {

                "risk_assessment":
                    customer.risk_category,

                "key_findings": [

                    f"Case ID: "
                    f"{latest_case.case_id}",

                    f"Status: "
                    f"{latest_case.status}",

                    f"Priority: "
                    f"{latest_case.priority}",

                    f"Investigator: "
                    f"{latest_case.investigator}",

                ],

                "recommendations": [],

                "conclusion":
                    "The latest case is "
                    f"{latest_case.case_id}.",
            }


        # ==================================================
        # AI ANALYSIS QUESTIONS
        # ==================================================

        prompt = PromptBuilder.build_chat_prompt(

            question=question,

            conversation=conversation,

            customer=customer,

            accounts=accounts,

            alerts=alerts,

            transactions=transactions,

            cases=cases,

            timeline=timeline,

        )


        response = self.llm.generate(
            prompt
        )


        return loads(response)