from functools import lru_cache
from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session

from config import Settings
from app.db.conn import SessionLocal


# Dependencies functions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@lru_cache()
def get_settings():
    return Settings()


# Dependency Annotations
DBSession = Annotated[Session, Depends(get_db)]
