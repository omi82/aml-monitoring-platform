from typing import Generic, Type, TypeVar

from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):

    def __init__(
        self,
        db: Session,
        model: Type[ModelType],
    ):
        self.db = db
        self.model = model

    def get_by_id(self, id_value):

        primary_key = list(self.model.__table__.primary_key.columns)[0]

        return (
            self.db.query(self.model)
            .filter(primary_key == id_value)
            .first()
        )

    def get_all(self):

        return self.db.query(self.model).all()

    def create(self, obj):

        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)

        return obj

    def delete(self, obj):

        self.db.delete(obj)
        self.db.commit()

    def update(self):

        self.db.commit()