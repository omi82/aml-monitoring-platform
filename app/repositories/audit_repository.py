from sqlalchemy.orm import Session

from app.models.audit_log import AuditLog


class AuditRepository:

    def __init__(self, db: Session):

        self.db = db

    def create(self, audit: AuditLog):

        self.db.add(audit)
        self.db.commit()
        self.db.refresh(audit)

        return audit

    def get_all(self):

        return (
            self.db.query(AuditLog)
            .order_by(AuditLog.created_at.desc())
            .all()
        )

    def get_by_user(self, username):

        return (
            self.db.query(AuditLog)
            .filter(AuditLog.username == username)
            .order_by(AuditLog.created_at.desc())
            .all()
        )