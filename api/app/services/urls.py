
from copy import copy
from sqlalchemy.orm import Session
from app.db.models.url import URL


def read_urls(db: Session):
    return db.query(URL).all()

def read_url(db: Session, id: int):
    return db.query(URL).filter(URL.id == id).first()

def read_urls_slice(db: Session, start: int = 0, end: int = 100):
    return db.query(URL).offset(start).limit(end).all()

def create_url(db: Session, url: dict):
    db_url = URL(**url.__dict__)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

