import datetime
from pydantic import BaseModel


class Photo(BaseModel):
    photo_id: int
    content: str
    post_id: int