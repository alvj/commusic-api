from sqlmodel import SQLModel, Field


class Category(SQLModel, table=True):
    __tablename__: str = "categories"

    id: int | None = Field(default=None, primary_key=True)
    name: str
