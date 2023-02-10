from fastapi import FastAPI
from .database import create_db_and_tables
from .routers import auth, users, posts


app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return "OK"
