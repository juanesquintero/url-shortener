from fastapi import APIRouter, BackgroundTasks
from app.shared.constants import Routes
from app.shared.dependencies import DBSession
# from app.schemas.url import Response
from app.services import urls as service

from asyncio import sleep

URL = APIRouter(prefix=f"/{Routes.urls}", tags=[Routes.urls])


async def get_page_title():
    print("Getting html page title...", flush=True)
    await sleep(5)
    print("Done!", flush=True)


# @URL.get("/", response_model=Response)
@URL.get("/")
async def list_all(db: DBSession):
    return service.read_urls(db)

# @URL.post("/shorten", response_model=Response)
@URL.post("/shorten")
async def shorten_url(tasks: BackgroundTasks):
    tasks.add_task(get_page_title)
    return {}
