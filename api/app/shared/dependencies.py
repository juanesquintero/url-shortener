from fastapi import Depends
from typing import Annotated
from functools import lru_cache
from sqlalchemy.orm import Session

from config import Settings
from app.db.conn import SessionLocal


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

DBSession = Annotated[Session, Depends(get_db)]
@lru_cache()
def get_settings():
    return Settings()
