from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel


if TYPE_CHECKING:
    from .post_model import Post


class PhotoBase(SQLModel):
    content: str


class Photo(PhotoBase, table=True):
    __tablename__: str = "photos"

    id: int | None = Field(default=None, primary_key=True)
    post_id: int = Field(index=True)

    post: "Post" = Relationship(back_populates="photos", sa_relationship_kwargs={
        "primaryjoin": "Post.id == foreign(Photo.post_id)"
    })


class PhotoRead(PhotoBase):
    id: int


class PhotoCreate(PhotoBase):
    post_id: int
