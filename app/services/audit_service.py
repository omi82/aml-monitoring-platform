from app.models.audit_log import AuditLog
from app.repositories.audit_repository import AuditRepository


class AuditService:

    def __init__(self, db):

        self.repository = AuditRepository(db)

    def log(
        self,
        username,
        action,
        entity,
        entity_id=None,
        details=None,
    ):
        """
        Create a new audit log entry.
        """

        audit = AuditLog(
            username=username,
            action=action,
            entity=entity,
            entity_id=entity_id,
            details=details,
        )

        return self.repository.create(audit)

    def log_action(
        self,
        current_user,
        action,
        entity,
        entity_id=None,
        details=None,
    ):
        """
        Log an action performed by the current authenticated user.
        """

        return self.log(
            username=current_user.username,
            action=action,
            entity=entity,
            entity_id=entity_id,
            details=details,
        )

    def get_all_logs(self):
        """
        Return all audit logs.
        """

        return self.repository.get_all()

    def get_user_logs(self, username):
        """
        Return audit logs for a specific user.
        """

        return self.repository.get_by_user(username)