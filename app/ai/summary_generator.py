class SummaryGenerator:

    @staticmethod
    def generate(case, alerts):

        summary = []

        summary.append(
            f"Case ID: {case.case_id}"
        )

        summary.append(
            f"Status: {case.status}"
        )

        summary.append(
            f"Priority: {case.priority}"
        )

        summary.append(
            f"Assigned Investigator: {case.investigator}"
        )

        summary.append("")

        summary.append("Triggered Alerts:")

        for alert in alerts:

            summary.append(
                f"- {alert.rule_name} (Risk Score: {alert.risk_score})"
            )

        highest = max(
            alerts,
            key=lambda x: x.risk_score,
        )

        summary.append("")

        summary.append(
            f"Highest Risk Rule: {highest.rule_name}"
        )

        summary.append(
            f"Overall Risk Score: {highest.risk_score}"
        )

        if highest.risk_score >= 90:

            summary.append(
                "Recommendation: Immediate investigation required."
            )

        elif highest.risk_score >= 75:

            summary.append(
                "Recommendation: High priority investigation."
            )

        else:

            summary.append(
                "Recommendation: Standard investigation."
            )

        return "\n".join(summary)