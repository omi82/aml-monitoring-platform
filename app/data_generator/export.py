from pathlib import Path

import pandas as pd

from app.utils.logger import get_logger

logger = get_logger(__name__)


class CSVExporter:
    """
    Export pandas DataFrames to CSV files.
    """

    @staticmethod
    def export(df: pd.DataFrame, file_path: Path) -> None:
        """
        Export a DataFrame to a CSV file.

        Args:
            df: DataFrame to export.
            file_path: Destination CSV file path.
        """

        # Create the output directory if it doesn't exist
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Export DataFrame
        df.to_csv(file_path, index=False)

        logger.info(
            "Exported %s rows -> %s",
            f"{len(df):,}",
            file_path,
        )