from datetime import datetime
from sqlmodel import Field, SQLModel


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


class UserRead(UserBase):
    id: int
    register_date: datetime
