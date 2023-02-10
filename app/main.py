from fastapi import FastAPI
from .database import create_db_and_tables
from .routers import auth, users, posts


app = FastAPI(
    title="Commusic"
)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(posts.router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/health")
def health_check():
    return "OK"
