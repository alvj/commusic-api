from datetime import datetime
from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .photo_model import Photo, PhotoRead
    from .user_model import User, UserReadBasic


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
    user: "User" = Relationship(back_populates="posts", sa_relationship_kwargs={
        "primaryjoin": "foreign(Post.user_id) == User.id",
        "uselist": False
    })


class PostRead(PostBase):
    id: int
    upload_date: datetime


class PostCreate(PostBase):
    pass


class PostReadWithDetails(PostRead):
    photos: list["PhotoRead"] | None = None
    user: "UserReadBasic"
