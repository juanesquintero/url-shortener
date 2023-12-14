from fastapi import APIRouter, BackgroundTasks, HTTPException, Request
from app.shared.constants import Routes
from app.shared.dependencies import DBSession, AppSettings
from app.schemas.url import Response
from app.services import urls as service
from app.controllers import urls as controller
from app.db.models.url import URL as model

URL = APIRouter(prefix=f"/{Routes.urls}", tags=[Routes.urls])


@URL.get("", response_model=Response)
async def list_all(db: DBSession):
    return {
        'detail': 'All URLs fetched',
        'data': service.read_urls(db)
    }

@URL.get("/top-100")
async def list_top_100(db: DBSession):
    return {
        'detail': 'Top 100 URLs fetched',
        'data': controller.get_top_100_urls(db)
    }

@URL.get("/{short_url}")
def access_to_url(short_url: str, db: DBSession):
    db_url = db.query(model).filter(model.shorted == short_url).first()
    if db_url:
        db_url.clicks += 1
        db.commit()
        return {"address": db_url.address}
    raise HTTPException(status_code=404, detail="URL not found")

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
