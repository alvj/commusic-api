from fastapi import Depends, FastAPI, HTTPException, status
from .database import create_db_and_tables
from .models import Post, PostCreate, PostRead, PostReadWithPhotos, Token, User, UserRead
from .dependencies import authenticate_user, create_access_token, get_current_user, get_session

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return "OK"

@app.get("/users/me", response_model=UserRead)
async def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user
