from os import environ
from sqlmodel import SQLModel, create_engine
from sqlalchemy.engine import URL

database_url = URL.create(
    environ["DB_ENGINE"],
    username=environ["USERNAME"],
    password=environ["PASSWORD"],
    host=environ["HOST"],
    database=environ["DATABASE"]
)

engine = create_engine(database_url)

def create_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_tables()
