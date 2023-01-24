import datetime
from pydantic import BaseModel


class PostCategory(BaseModel):
    post_id: int
    category_id: int