from fastapi import APIRouter, BackgroundTasks, HTTPException, Request
from app.shared.constants import Routes
from app.shared.dependencies import DBSession, AppSettings
from app.schemas.url import Response
from app.services import urls as service
from app.controllers import urls as controller
from app.db.models.url import URL as model

URL = APIRouter(prefix=f"/{Routes.urls}", tags=[Routes.urls])


@URL.get("/", response_model=Response)
async def list_all(
    db: DBSession, 
    short_url: str | None = None,
    original_url: str | None = None
):
    if short_url:
        return get_one(db, short_url=short_url)

    if original_url:
        return get_one(db, original_url=original_url)

    return {
        'detail': 'All URLs fetched',
        'data': service.read_urls(db)
    }

def get_one(db: DBSession, short_url: str = None, original_url: str = None):
    if original_url:
        db_url = service.read_shorted_url(db, short_url)
    else:
        db_url = service.read_url(db, original_url)

    if db_url:
        db_url.clicks += 1
        db.commit()
        return {
            'detail': 'Shorten URL found',
            'data': {
                'title': db_url.title,
                'address': db_url.address,
                'shorted': db_url.shorted,
                'clicks': db_url.clicks,
            }
        }
    raise HTTPException(status_code=404, detail="URL not found")


@URL.get("/top-100")
async def list_top_100(db: DBSession):
    return {
        'detail': 'Top 100 URLs fetched',
        'data': controller.get_top_100_urls(db)
    }

# @URL.post("/shorten", response_model=Response)
@URL.post("/shorten", response_model=dict)
async def shorten_url(
    original_url: str,
    request: Request,
    db: DBSession,
    settings: AppSettings,
    tasks: BackgroundTasks,
):
    existing_url = service.read_url(db, original_url)
    if existing_url:
        return {
            'detail': 'URL already saved',
            'data': existing_url.__dict__
        }

    tasks.add_task(controller.get_page_title, original_url=original_url)
    db_url = controller.create_shorten_url(db, request, settings.error_logger, original_url)

    if db_url:
        return {
            'detail': 'URL shorten added successfully',
            'data': db_url.__dict__
        }

    return {
        'detail': 'Failed adding shorten URL',
        'data': None
    }
