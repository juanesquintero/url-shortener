from functools import lru_cache
from config import Settings
from app.db.conn import SessionLocal


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@lru_cache()
def get_settings():
    return Settings()
