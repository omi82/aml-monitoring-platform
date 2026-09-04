class RiskEngine:

    @staticmethod
    def calculate(
        customer,
        alerts,
        transactions,
    ):

        score = 0

        reasons = []


        # ==================================================
        # CUSTOMER RISK CATEGORY
        # ==================================================

        if customer.risk_category == "HIGH":

            score += 40

            reasons.append(
                "Customer belongs to HIGH risk category."
            )


        elif customer.risk_category == "MEDIUM":

            score += 20

            reasons.append(
                "Customer belongs to MEDIUM risk category."
            )


        elif customer.risk_category == "LOW":

            reasons.append(
                "Customer belongs to LOW risk category."
            )


        # ==================================================
        # AML ALERTS
        # ==================================================

        if len(alerts) >= 3:

            score += 30

            reasons.append(
                f"{len(alerts)} AML alerts detected."
            )


        elif len(alerts) > 0:

            score += 15

            reasons.append(
                f"{len(alerts)} AML alert(s) detected."
            )


        # ==================================================
        # LARGE TRANSACTIONS
        # ==================================================

        high_value = [

            tx

            for tx in transactions

            if float(tx.amount) >= 100000

        ]


        if high_value:

            score += 20

            reasons.append(
                f"{len(high_value)} high-value "
                "transactions found."
            )


        # ==================================================
        # TRANSACTION ACTIVITY
        # ==================================================

        if len(transactions) >= 20:

            score += 10

            reasons.append(
                "High transaction activity."
            )


        # ==================================================
        # LIMIT SCORE
        # ==================================================

        score = min(
            score,
            100,
        )


        # ==================================================
        # RISK CATEGORY
        # ==================================================
        #
        # The customer's institutional risk category
        # remains the authoritative risk classification.
        #
        # The numerical score is a separate indicator.
        #

        risk = (
            customer.risk_category
            or "UNKNOWN"
        ).upper()


        return (
            risk,
            score,
            reasons,
        )