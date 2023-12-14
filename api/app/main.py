from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import Root
from config import APP_CONFIG
from app.shared.utils.http import AppHTTPException
from app.shared.dependencies import catch_exceptions_middleware

# from app.routers import ROUTERS

app = FastAPI(**APP_CONFIG)

# App origins access
origins = ['http://localhost:3000']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=origins,
    allow_headers=origins,
)

# Code Exception
app.middleware('http')(catch_exceptions_middleware)
@app.exception_handler(AppHTTPException)
async def app_exception_handler(
    request: Request,
    exc: AppHTTPException
):
    body = exc.__dict__.copy()
    return JSONResponse(
        status_code=body.pop('status_code'),
        content=body
    )


# Root/Index path
@app.get('/', tags=['index'], response_model=Root)
async def index() -> dict:
    '''
    Root path get function
    :return: {'api': 'URL Shortener'}
    '''
    return {'api': 'URL Shortener'}


# Routes App
# for router in ROUTERS:
#     app.include_router(router)
