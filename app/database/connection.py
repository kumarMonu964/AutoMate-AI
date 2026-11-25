from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATABASE_PATH = (
    PROJECT_ROOT 
    / "storage"
    / "sqlite"
    / "automate.db"
)

# Ensure the database directory exists
DATABASE_PATH.parent.mkdir(
    parents=True,
    exist_ok=True
)

DATABASE_URL = f"sqlite:///{DATABASE_PATH.as_posix()}"

# Base class for all database models
class Base(DeclarativeBase):
    pass

# Create database engine
engine = create_engine(
    DATABASE_URL,
    connect_args = {"check_same_thread": False}
)

# Create database session factory
SessionLocal = sessionmaker(
    bind = engine,
    autoflush = False,
    autocommit = False
)

def get_db():
    """
    Provide a database session
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()