import datetime
import dataclasses
from pydantic import BaseModel

@dataclasses.dataclass
class Post(BaseModel):
    """A dummy docstring."""
    post_id: int
    user_id: int
    price: int
    title: str
    upload_date: datetime.date
    description: str
