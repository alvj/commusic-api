from fastapi import FastAPI, status
from sqlmodel import Session, select
from .database import engine
from .models import Post

app = FastAPI()

@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return "Health check OK"

@app.get("/posts")
def read_posts() -> list[Post]:
    with Session(engine) as session:
        posts = session.exec(select(Post)).all()
    return posts
