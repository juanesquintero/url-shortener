
import string
from asyncio import sleep

from app.services import urls as service

def generate_short_url(_id: int) -> str:
    characters = string.ascii_letters + string.digits
    base = len(characters)
    result = ""

    while _id > 0:
        _id, remainder = divmod(_id, base)
        result = characters[remainder] + result

    return result or "0"


async def get_page_title():
    print("Getting html page title...", flush=True)
    await sleep(5)
    print("Done!", flush=True)

def create_shorten_url(db, request, error_logger, original_url):
    # Insert row and get autoincrement id
    db_url = service.create_url(db, original_url)
    try:
        # Update the short URL with the generated one
        url_id = generate_short_url(db_url.id)
        db_url.short_url = f'{request.base_url}{url_id}'
        db.commit()
        return db_url
    except Exception as e:
        error_logger.error(str(e))
        db.rollback()
        return None


def get_top_100_urls(db):
    return service.read_urls_slice(db, end=100)
