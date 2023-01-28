import dataclasses
from pydantic import BaseModel

@dataclasses.dataclass
class Photo(BaseModel):
    """Photo Model."""
    photo_id: int
    content: str
    post_id: int
