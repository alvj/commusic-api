from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel

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

class PostCreate(PostBase):
    pass

class PhotoBase(SQLModel):
    content: str
    post_id: int = Field(index=True)

class Photo(PhotoBase, table=True):
    __tablename__: str = "photos"

    id: int | None = Field(default=None, primary_key=True)
    post: Post = Relationship(back_populates="photos", sa_relationship_kwargs={
        "primaryjoin": "Post.id == foreign(Photo.post_id)"
    })

class PhotoRead(PhotoBase):
    id: int

class PhotoCreate(PhotoBase):
    pass

class PostCategory(SQLModel, table=True):
    __tablename__: str = "posts_categories"

    id: int | None = Field(default=None, primary_key=True)
    post_id: int
    category_id: int

class Category(SQLModel, table=True):
    __tablename__: str = "categories"

    id: int | None = Field(default=None, primary_key=True)
    name: str

class PostReadWithPhotos(PostRead):
    photos: list[PhotoRead] | None = None

# AUTHENTICATION
class UserBase(SQLModel):
    username: str = Field(index=True)
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

class UserRead(UserBase):
    id: int
    register_date: datetime

class Token(SQLModel):
    access_token: str
    token_type: str
