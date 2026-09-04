import pandas as pd


class DataValidator:
    """
    Validate datasets before loading.
    """

    @staticmethod
    def check_missing(df: pd.DataFrame):

        missing = df.isnull().sum()

        return missing[missing > 0]

    @staticmethod
    def check_duplicates(df: pd.DataFrame):

        return int(df.duplicated().sum())

    @staticmethod
    def validate(df: pd.DataFrame):

        return {
            "rows": len(df),
            "columns": len(df.columns),
            "duplicates": DataValidator.check_duplicates(df),
            "missing": DataValidator.check_missing(df),
        }