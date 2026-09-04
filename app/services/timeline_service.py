from app.models.case_timeline import CaseTimeline
from app.repositories.timeline_repository import TimelineRepository


class TimelineService:

    def __init__(self, db):

        self.repository = TimelineRepository(db)

    def create_entry(
        self,
        case_id,
        action,
        performed_by,
        old_value=None,
        new_value=None,
        comments=None,
    ):

        timeline = CaseTimeline(
            case_id=case_id,
            action=action,
            performed_by=performed_by,
            old_value=old_value,
            new_value=new_value,
            comments=comments,
        )

        return self.repository.create(timeline)

    def get_case_timeline(self, case_id):

        return self.repository.get_by_case(case_id)

    def get_all(self):

        return self.repository.get_all()