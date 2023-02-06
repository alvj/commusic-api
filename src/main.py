from fastapi import Depends, FastAPI, HTTPException, status
from sqlmodel import Session, select
from .database import create_db_and_tables, engine
from .models import Post, PostCreate, PostRead, PostReadWithPhotos

def get_session():
    with Session(engine) as session:
        yield session

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return "OK"

@app.post("/posts", response_model=PostRead)
def create_post(post: PostCreate, session: Session = Depends(get_session)):
    db_post = Post.from_orm(post)
    session.add(db_post)
    session.commit()
    session.refresh(db_post)
    return db_post

@app.get("/posts", response_model=list[PostRead])
def read_posts(session: Session = Depends(get_session)) :
    posts = session.exec(select(Post)).all()
    return posts

@app.get("/posts/{post_id}", response_model=PostReadWithPhotos)
def read_post_details(post_id: int, session: Session = Depends(get_session)):
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post

@app.delete("/posts/{post_id}")
def delete_post(post_id: int, session: Session = Depends(get_session)):
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    session.delete(post)
    session.commit()
