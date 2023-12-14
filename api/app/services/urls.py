
from sqlalchemy.orm import Session
from app.db.models.url import URL

def read_urls(db: Session):
    return db.query(URL).all()

def read_url(db: Session, original_url: str):
    return db.query(URL).filter(URL.address == original_url).first()

def read_urls_slice(db: Session, start: int = 0, end: int = 100):
    return db.query(URL).offset(start).limit(end).all()

def create_url(db: Session,  original_url: str):
    db_url = URL(address=original_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url
