import dataclasses
from pydantic import BaseModel

@dataclasses.dataclass
class PostCategory(BaseModel):
    """Post Category Model."""
    post_id: int
    category_id: int
