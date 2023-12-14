from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import Root
from config import APP_CONFIG

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
