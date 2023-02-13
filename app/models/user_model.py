from datetime import datetime
from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, SQLModel, Relationship

if TYPE_CHECKING:
    from .post_model import Post, PostRead


class UserBase(SQLModel):
    username: str = Field(unique=True)
    email: str
    full_name: str
    description: str | None = Field(default=None)
    birth_date: datetime | None = Field(default=None)
    profile_picture: str | None = Field(default=None)


class User(UserBase, table=True):
    __tablename__: str = "users"

    id: int | None = Field(default=None, primary_key=True)
    register_date: datetime | None = Field(default_factory=datetime.utcnow)
    password: str

    posts: list["Post"] | None = Relationship(back_populates="user", sa_relationship_kwargs={
        "primaryjoin": "foreign(Post.user_id) == User.id"
    })


class UserRead(UserBase):
    id: int
    register_date: datetime


class UserReadWithDetails(UserRead):
    posts: Optional[list["PostRead"]]


class UserReadBasic(SQLModel):
    username: str
    email: str
    full_name: str
    profile_picture: str | None


class UserCreate(UserBase):
    password: str
