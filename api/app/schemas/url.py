from pydantic import BaseModel
from typing import TypedDict


class URLSchema(BaseModel):
    title: str | None
    address: str
    shorted: str | None
    access_count: int | None

    class Config:
        orm_mode = True

class Response(TypedDict):
    data: URLSchema | list[URLSchema]
    detail: str | None
