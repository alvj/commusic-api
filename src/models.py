from datetime import datetime
from sqlmodel import Field, SQLModel

class Post(SQLModel, table=True):
    __tablename__: str = "posts"

    post_id: int | None = Field(default=None, primary_key=True)
    user_id: int
    title: str
    description: str
    price: int
    upload_date: datetime

class Photo(SQLModel):
    __tablename__: str = "photos"

    photo_id: int | None = Field(default=None, primary_key=True)
    content: str
    post_id: int

class PostCategory(SQLModel):
    __tablename__: str = "posts_categories"

    post_id: int
    category_id: int

class Category(SQLModel):
    __tablename__: str = "categories"

    category_id: int | None = Field(default=None, primary_key=True)
    category_name: str
