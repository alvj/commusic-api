from datetime import datetime
from sqlmodel import Field, SQLModel

class Post(SQLModel, table=True):
    __tablename__: str = "posts"

    id: int | None = Field(default=None, primary_key=True)
    user_id: int
    photos: list["Photo"] | None = Relationship(back_populates="post", sa_relationship_kwargs={
        "primaryjoin": "Post.id == foreign(Photo.post_id)"
    })
    upload_date: datetime = Field(default=datetime.now)

class Photo(SQLModel):
    __tablename__: str = "photos"

    id: int | None = Field(default=None, primary_key=True)
    post: Post = Relationship(back_populates="photos", sa_relationship_kwargs={
        "primaryjoin": "Post.id == foreign(Photo.post_id)"
    })

class PostCategory(SQLModel):
    __tablename__: str = "posts_categories"

    post_id: int
    category_id: int

class Category(SQLModel):
    __tablename__: str = "categories"

    id: int | None = Field(default=None, primary_key=True)
    name: str
