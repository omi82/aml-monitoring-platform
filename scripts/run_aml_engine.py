from app.database.session import SessionLocal
from app.services.aml_processing_service import AMLProcessingService


def main():

    db = SessionLocal()

    try:

        service = AMLProcessingService(db)

        summary = service.process()

        print("\n")
        print("=" * 60)
        print("AML EXECUTION SUMMARY")
        print("=" * 60)

        print(
            f"Transactions Processed : {summary['transactions']:,}"
        )

        print(
            f"Rules Executed         : {summary['rules']}"
        )

        print(
            f"Alerts Generated       : {summary['generated_alerts']:,}"
        )

        print(
            f"New Alerts Saved       : {summary['saved_alerts']:,}"
        )

        print(
            f"Execution Time         : {summary['execution_time']:.2f} sec"
        )

        print("=" * 60)

    finally:
        db.close()


if __name__ == "__main__":
    main()