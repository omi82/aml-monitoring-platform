from sqlalchemy.orm import Session

from app.models.case_timeline import CaseTimeline


class TimelineRepository:

    def __init__(self, db: Session):

        self.db = db

    def create(self, timeline: CaseTimeline):

        self.db.add(timeline)
        self.db.commit()
        self.db.refresh(timeline)

        return timeline

    def get_by_case(self, case_id):

        return (
            self.db.query(CaseTimeline)
            .filter(CaseTimeline.case_id == case_id)
            .order_by(CaseTimeline.created_at.asc())
            .all()
        )

    def get_all(self):

        return (
            self.db.query(CaseTimeline)
            .order_by(CaseTimeline.created_at.desc())
            .all()
        )