
import string
from sqlalchemy.orm import Session
from app.db.models.url import URL


def read_urls(db: Session):
    return db.query(URL).all()

def read_url(db: Session, _id: int):
    return db.query(URL).filter(URL.id == _id).first()

def read_urls_slice(db: Session, start: int = 0, end: int = 100):
    return db.query(URL).offset(start).limit(end).all()

def create_url(db: Session,  original_url: str):
    db_url = URL(original_url=original_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)

    # Update the short URL with the generated one
    db_url.short_url = generate_short_url(db_url.id)
    db.commit()

    return db_url
def generate_short_url(_id: int) -> str:
    characters = string.ascii_letters + string.digits
    base = len(characters)
    result = ""

    while _id > 0:
        _id, remainder = divmod(_id, base)
        result = characters[remainder] + result

    return result or "0"
