import dataclasses
from pydantic import BaseModel

@dataclasses.dataclass
class PostCategory(BaseModel):
    """A dummy docstring."""
    post_id: int
    category_id: int
