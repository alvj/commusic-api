import datetime
import dataclasses
from sqlmodel import Field, SQLModel

@dataclasses.dataclass
class Post(SQLModel, table=True):
    """Post Model."""
    post_id: int = Field(primary_key=True)
    user_id: int
    price: int
    title: str
    upload_date: datetime.date
    description: str
