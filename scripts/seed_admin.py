from app.database.session import SessionLocal
from app.seeds.user_seed import seed_admin_user

db = SessionLocal()

try:
    seed_admin_user(db)
finally:
    db.close()