import datetime
from pydantic import BaseModel


class Post(BaseModel):
    post_id: int
    user_id: int
    price: int
    title: str
    upload_date: datetime.date
    description: str