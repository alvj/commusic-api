import dataclasses
from pydantic import BaseModel

@dataclasses.dataclass
class Category(BaseModel):
    """Category Model."""
    category_name: str
    category_id: int
