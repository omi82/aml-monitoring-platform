import pandas as pd


class DataTransformer:
    """
    Transform raw datasets into warehouse-ready datasets.
    """

    @staticmethod
    def normalize_column_names(df: pd.DataFrame) -> pd.DataFrame:
        """
        Convert column names to lowercase and replace spaces with underscores.
        """
        df = df.copy()

        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        return df

    @staticmethod
    def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
        """
        Remove duplicate rows.
        """
        return df.drop_duplicates()

    @staticmethod
    def trim_string_columns(df: pd.DataFrame) -> pd.DataFrame:
        """
        Remove leading/trailing spaces from string columns.
        """
        df = df.copy()

        object_columns = df.select_dtypes(include="object").columns

        for column in object_columns:
            df[column] = df[column].str.strip()

        return df

    @staticmethod
    def transform(df: pd.DataFrame) -> pd.DataFrame:

        df = DataTransformer.normalize_column_names(df)

        df = DataTransformer.trim_string_columns(df)

        df = DataTransformer.remove_duplicates(df)

        return df