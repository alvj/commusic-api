from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select
from .database import create_db_and_tables
from .models import Post, PostCreate, PostRead, PostReadWithPhotos, Token, User, UserBase
from .dependencies import authenticate_user, create_access_token, get_current_user, get_session

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

@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token = create_access_token(data={"sub": user.get("username")})
    return Token(access_token=access_token, token_type="bearer")

@app.get("/users/me", response_model=UserBase)
async def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user
