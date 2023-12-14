from pydantic import BaseModel
from typing import TypedDict


class URLSchema(TypedDict):
    title: str | None
    address: str
    shorted: str | None
    access_count: int | None


class Response(TypedDict):
    data: URLSchema | list[URLSchema]
    detail: str | None
