from fastapi import FastAPI
from sqlalchemy import text

from .api import books, categories
from .db.db import Base, SessionLocal, engine
from .db import models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Octagon API")

app.include_router(categories.router)
app.include_router(books.router)


@app.get("/")
def read_root():
    return {"message": "Octagon API is running"}


@app.on_event("startup")
def startup_check():
    db = SessionLocal()
    try:
        db.execute(text("SELECT 1"))
    finally:
        db.close()


@app.get("/health")
def health_check():
    return {"status": "ok"}
