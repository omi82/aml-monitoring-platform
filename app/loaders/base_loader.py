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

    Loads DataFrame records in batches without creating
    the entire dataset as SQLAlchemy objects in memory.
    """

    def __init__(self, db: Session):

        self.db = db


    def load_dataframe(
        self,
        model,
        dataframe: DataFrame,
    ) -> None:

        total = len(dataframe)

        if total == 0:

            logger.warning(
                "No records found."
            )

            return


        start_time = perf_counter()


        try:

            for start in range(
                0,
                total,
                ETL_BATCH_SIZE,
            ):

                end = min(
                    start + ETL_BATCH_SIZE,
                    total,
                )


                # Convert only the current batch
                # into dictionaries.
                batch_dataframe = dataframe.iloc[
                    start:end
                ]


                records = (
                    batch_dataframe
                    .to_dict(
                        orient="records"
                    )
                )


                # Use bulk_insert_mappings instead
                # of creating SQLAlchemy objects.
                self.db.bulk_insert_mappings(
                    model,
                    records,
                )


                self.db.commit()


                logger.info(
                    "Loaded %s/%s records",
                    end,
                    total,
                )


            elapsed = (
                perf_counter()
                - start_time
            )


            logger.info(
                "Finished loading %s rows in %.2f seconds.",
                total,
                elapsed,
            )


        except SQLAlchemyError as error:

            self.db.rollback()

            logger.exception(error)

            raise