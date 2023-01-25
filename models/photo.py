import dataclasses
from pydantic import BaseModel

@dataclasses.dataclass
class Photo(BaseModel):
    """A dummy docstring."""
    photo_id: int
    content: str
    post_id: int
