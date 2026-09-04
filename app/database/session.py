from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Create the SQLAlchemy engine
engine = create_engine(
    settings.database_url,
    echo=False,
)

# Create a session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db():
    """
    Dependency for FastAPI endpoints.
    Yields a database session and ensures it is closed.
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()