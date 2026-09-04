from time import perf_counter

from pandas import DataFrame
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.core.constants import ETL_BATCH_SIZE
from app.utils.logger import get_logger

logger = get_logger(__name__)


class BaseLoader:
    """
    Generic SQLAlchemy Data Loader.
    """

    def __init__(self, db: Session):
        self.db = db

    def load_dataframe(
        self,
        model,
        dataframe: DataFrame,
    ) -> None:

        records = [
            model(**row)
            for row in dataframe.to_dict(
                orient="records"
            )
        ]

        total = len(records)

        if total == 0:
            logger.warning("No records found.")

            return

        start_time = perf_counter()

        try:

            for start in range(
                0,
                total,
                ETL_BATCH_SIZE,
            ):

                batch = records[
                    start:start + ETL_BATCH_SIZE
                ]

                self.db.bulk_save_objects(batch)

                self.db.commit()

                logger.info(
                    "Loaded %s/%s records",
                    min(start + ETL_BATCH_SIZE, total),
                    total,
                )

            elapsed = perf_counter() - start_time

            logger.info(
                "Finished loading %s rows in %.2f seconds.",
                total,
                elapsed,
            )

        except SQLAlchemyError as error:

            self.db.rollback()

            logger.exception(error)

            raise