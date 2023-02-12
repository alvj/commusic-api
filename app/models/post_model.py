from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .photo_model import Photo, PhotoRead


class PostBase(SQLModel):
    user_id: int = Field(index=True)
    title: str
    description: str
    price: int


class Post(PostBase, table=True):
    __tablename__: str = "posts"

    id: int | None = Field(default=None, primary_key=True)
    upload_date: datetime | None = Field(default_factory=datetime.utcnow)
    photos: list["Photo"] | None = Relationship(back_populates="post", sa_relationship_kwargs={
        "primaryjoin": "Post.id == foreign(Photo.post_id)"
    })


class PostRead(PostBase):
    id: int
    upload_date: datetime


class PostCreate(PostBase):
    pass


class PostReadWithPhotos(PostRead):
    photos: list["PhotoRead"] | None = None
