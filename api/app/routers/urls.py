from fastapi import APIRouter
from app.shared.constants import Routes
from app.shared.dependencies import DBSession
from app.schemas.url import Response
from app.services import urls as service

from asyncio import sleep

URL = APIRouter(prefix=f"/{Routes.urls}", tags=[Routes.urls])


async def get_page_title():
    print("Getting html page title...")
    await sleep(10)
    print("Done!")


# @URL.get("/", response_model=Response)
@URL.get("/")
async def list_all(db: DBSession):
    return service.read_urls(db)

@URL.post("/shorten", response_model=Response)
async def shorten_url():
    return {}
