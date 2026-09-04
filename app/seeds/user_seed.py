from sqlalchemy.orm import Session

from app.auth.password import hash_password
from app.models.user import User


def seed_admin_user(db: Session):

    existing = (
        db.query(User)
        .filter(User.username == "admin")
        .first()
    )

    if existing:
        print("Admin user already exists.")
        return

    admin = User(
        username="admin",
        email="admin@aml.local",
        full_name="System Administrator",
        hashed_password=hash_password("Admin@123"),
        role="Admin",
        is_active=True,
    )

    db.add(admin)
    db.commit()

    print("Admin user created successfully.")