
import string
import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session

from app.services import urls as service

def generate_short_url(_id: int) -> str:
    characters = string.ascii_letters + string.digits
    base = len(characters)
    result = ""

    while _id > 0:
        _id, remainder = divmod(_id, base)
        result = characters[remainder] + result

    return result or "0"


async def get_page_title(db: Session, url: str):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title_tag = soup.find('title')
            if title_tag:
                db_url = service.read_url(db, url)
                db_url.title = title_tag.text.strip()
                db.commit()
                print(f"Fetched title! {db_url.title}", flush=True)
            else:
                print(f"No title tag found on the page: \n {url}", flush=True)
        else:
            print(f"Error fetch response on: \n {url}", flush=True)

    except Exception as e:
        print(f"Error: getting title tag {url} \n {str(e)}", flush=True)

def create_shorten_url(db: Session, request, error_logger, original_url):
    # Insert row and get autoincrement id
    db_url = service.create_url(db, original_url)
    try:
        # Update the short URL with the generated one
        url_id = generate_short_url(db_url.id)
        db_url.shorted = f'{request.base_url}{url_id}'
        db.commit()
        return db_url
    except Exception as e:
        error_logger.error(str(e))
        db.rollback()
        return None


def get_top_urls(db, limit):
    ordered_by_clicks = service.read_top_clicks(db)
    return service.read_urls_slice(ordered_by_clicks, end=limit)
