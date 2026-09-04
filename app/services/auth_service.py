from app.auth.jwt import create_access_token
from app.auth.password import verify_password
from app.repositories.user_repository import UserRepository
from app.services.audit_service import AuditService


class AuthService:

    def __init__(self, db):

        self.db = db
        self.user_repository = UserRepository(db)

    def login(
        self,
        username: str,
        password: str,
    ):

        user = self.user_repository.get_by_username(username)

        if user is None:
            return None

        if not verify_password(
            password,
            user.hashed_password,
        ):
            return None

        AuditService(self.db).log(
            username=user.username,
            action="LOGIN",
            entity="User",
            entity_id=user.username,
            details="User logged in successfully",
        )

        token = create_access_token(
            {
                "sub": str(user.user_id),
                "username": user.username,
                "role": user.role,
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer",
        }