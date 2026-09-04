class ETLReport:

    @staticmethod
    def print_report(report: dict):

        print("=" * 40)

        print("ETL VALIDATION REPORT")

        print("=" * 40)

        print(f"Rows       : {report['rows']}")

        print(f"Columns    : {report['columns']}")

        print(f"Duplicates : {report['duplicates']}")

        print("\nMissing Values")

        print(report["missing"])

        print("=" * 40)