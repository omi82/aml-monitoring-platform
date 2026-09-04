AML_RULES = {
    "large_value_transaction": {
        "threshold": 90000,
        "risk_score": 85,
        "severity": "High",
    },


    "velocity": {
        "transaction_count": 5,
        "time_window_minutes": 30,
        "risk_score": 90,
        "severity": "High",
    },

    "high_risk_country": {
        "risk_score": 95,
        "severity": "Critical",
    },

    "structuring": {
        "threshold": 90000,
        "occurrences": 5,
        "hours": 24,
        "risk_score": 92,
        "severity": "High",
    },

    "dormant_account": {
        "inactive_days": 180,
        "threshold": 500000,
        "risk_score": 97,
        "severity": "Critical",
    }
}