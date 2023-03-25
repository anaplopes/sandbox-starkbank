from src.settings import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


def engine():
    return create_engine(settings.DB_URI)


def session():
    return sessionmaker(autocommit=False, autoflush=False, bind=engine())


def db_connection():
    db = scoped_session(session())
    try:
        yield db
    finally:
        db.close()
