from fastapi import Depends, FastAPI, HTTPException, status
from sqlmodel import Session, select
from .database import create_db_and_tables, engine
from .models import Post
def get_session():
    with Session(engine) as session:
        yield session

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return "Health check OK"

@app.get("/posts")
def read_posts() -> list[Post]:
    with Session(engine) as session:
        posts = session.exec(select(Post)).all()
    return posts
