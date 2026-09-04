class RecommendationEngine:

    @staticmethod
    def generate(
        risk: str,
        alerts,
        cases,
    ):

        if risk == "HIGH":

            if len(cases) > 0:
                return (
                    "Escalate investigation to Level 2 "
                    "and perform Enhanced Due Diligence (EDD)."
                )

            return (
                "Create an investigation case immediately."
            )

        if risk == "MEDIUM":

            return (
                "Continue monitoring and review "
                "recent customer activity."
            )

        return (
            "No immediate action required. "
            "Continue routine monitoring."
        )