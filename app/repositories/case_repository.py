from datetime import datetime

from sqlalchemy.orm import Session

from app.models.case import Case
from sqlalchemy import asc, desc


class CaseRepository:

    def __init__(self, db: Session):

        self.db = db

    def create(self, case: Case):

        self.db.add(case)
        self.db.commit()
        self.db.refresh(case)

        return case

    def get_all(
        self,
        filters,
    ):

        query = self.db.query(Case)

        if filters.status:
            query = query.filter(
                Case.status == filters.status
            )

        if filters.priority:
            query = query.filter(
                Case.priority == filters.priority
            )

        if filters.investigator:
            query = query.filter(
                Case.investigator == filters.investigator
            )

        sort_column = getattr(
            Case,
            filters.sort_by,
        )

        if filters.sort_order == "asc":
            query = query.order_by(
                asc(sort_column)
            )
        else:
            query = query.order_by(
                desc(sort_column)
            )

        return (
            query
            .offset((filters.page - 1) * filters.size)
            .limit(filters.size)
            .all()
        )

    def update(self, case):

        self.db.commit()
        self.db.refresh(case)

        return case

    def get_by_id(self, case_id):

        return (
            self.db.query(Case)
            .filter(Case.case_id == case_id)
            .first()
        )

    def get_by_alert(self, alert_key):

        return (
            self.db.query(Case)
            .filter(Case.alert_key == alert_key)
            .first()
        )

    def get_open_cases(self):

        return (
            self.db.query(Case)
            .filter(Case.status != "Closed")
            .all()
        )

    def update(self, case):

        self.db.commit()
        self.db.refresh(case)

        return case

    def delete(self, case: Case):

        self.db.delete(case)
        self.db.commit()

    def assign_case(
        self,
        case,
        investigator,
        assigned_by,
    ):

        case.investigator = investigator
        case.assigned_by = assigned_by
        case.assigned_at = datetime.utcnow()
        case.status = "Assigned"

        self.db.commit()
        self.db.refresh(case)

        return case


    def update(self, case):

        self.db.commit()
        self.db.refresh(case)

        return case


    def add_comment(
        self,
        case,
        comment,
    ):

        case.comments = comment

        self.db.commit()
        self.db.refresh(case)

        return case