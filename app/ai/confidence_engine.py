class ConfidenceEngine:

    @staticmethod
    def calculate(
        customer,
        alerts,
        transactions,
        cases,
    ):

        confidence = 50

        if customer.risk_category == "HIGH":
            confidence += 15

        confidence += min(len(alerts) * 5, 15)

        confidence += min(len(transactions) // 10, 10)

        confidence += min(len(cases) * 5, 10)

        return min(confidence, 99)