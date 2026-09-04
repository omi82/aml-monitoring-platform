from app.aml_engine.engine import AMLRuleEngine


def main():

    transaction = {
        "transaction_id": "TXN1001",
        "amount": 15000,
        "transaction_type": "Cash",
    }

    engine = AMLRuleEngine()

    alerts = engine.evaluate(transaction)

    print(alerts)


if __name__ == "__main__":
    main()