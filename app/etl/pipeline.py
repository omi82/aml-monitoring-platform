from pathlib import Path

from app.core.constants import (
    PROCESSED_ACCOUNTS_FILE,
    PROCESSED_CUSTOMERS_FILE,
    PROCESSED_TRANSACTIONS_FILE,
    RAW_ACCOUNTS_FILE,
    RAW_CUSTOMERS_FILE,
    RAW_TRANSACTIONS_FILE,
)
from app.data_generator.export import CSVExporter
from app.etl.extract import DataExtractor
from app.etl.report import ETLReport
from app.etl.transform import DataTransformer
from app.etl.validate import DataValidator
from app.utils.logger import get_logger

logger = get_logger(__name__)


class ETLPipeline:
    """
    Enterprise ETL Pipeline

    Pipeline Flow

    Extract
        ↓
    Transform
        ↓
    Validate
        ↓
    Export Processed Data
    """

    def process_dataset(
        self,
        raw_file: Path,
        processed_file: Path,
    ) -> None:
        """
        Process a single dataset through the ETL pipeline.
        """

        logger.info("Processing %s", raw_file.name)

        # -------------------------
        # Extract
        # -------------------------
        df = DataExtractor.read_csv(raw_file)

        # -------------------------
        # Transform
        # -------------------------
        df = DataTransformer.transform(df)

        # -------------------------
        # Validate
        # -------------------------
        report = DataValidator.validate(df)
        ETLReport.print_report(report)

        # -------------------------
        # Export
        # -------------------------
        CSVExporter.export(
            df,
            processed_file,
        )

        logger.info(
            "Finished processing %s",
            processed_file.name,
        )

    def run(self) -> None:
        """
        Run the ETL pipeline for all datasets.
        """

        logger.info("Starting Enterprise ETL Pipeline...")

        datasets = [
            (
                RAW_CUSTOMERS_FILE,
                PROCESSED_CUSTOMERS_FILE,
            ),
            (
                RAW_ACCOUNTS_FILE,
                PROCESSED_ACCOUNTS_FILE,
            ),
            (
                RAW_TRANSACTIONS_FILE,
                PROCESSED_TRANSACTIONS_FILE,
            ),
        ]

        for raw_file, processed_file in datasets:
            self.process_dataset(
                raw_file,
                processed_file,
            )

        logger.info("Enterprise ETL Pipeline Completed Successfully.")