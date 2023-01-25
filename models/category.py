import dataclasses
from pydantic import BaseModel

@dataclasses.dataclass
class Category(BaseModel):
    """A dummy docstring."""
    category_name: str
    category_id: int
