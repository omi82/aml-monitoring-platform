from pathlib import Path

import pandas as pd
from app.utils.logger import get_logger

logger = get_logger(__name__)

class DataExtractor:
    """
    Extract datasets from CSV files.
    """

    @staticmethod
    def read_csv(file_path: Path) -> pd.DataFrame:

        logger.info("Reading %s", file_path.name)

        return pd.read_csv(file_path)