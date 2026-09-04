from sqlalchemy.orm import Session

from app.utils.logger import get_logger

logger = get_logger(__name__)


class Seeder:
    """
    Generic Database Seeder.
    """

    def __init__(self, db: Session):
        self.db = db

    def seed(self, model, records):
        """
        Insert master data only if table is empty.
        """

        exists = self.db.query(model).first()

        if exists:
            logger.info("%s already seeded.", model.__tablename__)
            return

        objects = [
            model(**record)
            for record in records
        ]

        self.db.add_all(objects)

        self.db.commit()

        logger.info(
            "Inserted %s records into %s",
            len(objects),
            model.__tablename__,
        )