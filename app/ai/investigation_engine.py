from app.ai.risk_engine import RiskEngine
from app.ai.recommendation_engine import RecommendationEngine
from app.ai.confidence_engine import ConfidenceEngine


class InvestigationEngine:

    @staticmethod
    def analyze(

        customer,

        transactions,

        alerts,

        cases,

    ):

        risk, score, reasons = RiskEngine.calculate(

            customer,

            alerts,

            transactions,

        )

        recommendation = RecommendationEngine.generate(

            risk,

            alerts,

            cases,

        )

        confidence = ConfidenceEngine.calculate(

            customer,

            alerts,

            transactions,

            cases,

        )

        return {

            "risk": risk,

            "score": score,

            "confidence": confidence,

            "recommendation": recommendation,

            "reasons": reasons,

        }