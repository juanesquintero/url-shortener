from pydantic import BaseModel


class Root(BaseModel):
    api: str
