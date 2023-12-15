from pydantic import BaseModel
from typing import TypedDict


class URLSchema(BaseModel):
    id: int | None
    title: str | None
    address: str
    shorted: str | None
    clicks: int | None

    class Config:
        orm_mode = True

class URLResponse(TypedDict):
    data: URLSchema | list[URLSchema] | None
    detail: str | None
