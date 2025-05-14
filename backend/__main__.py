from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tinydb import TinyDB

from .handler import get_router
from .repository import get_repository

app = FastAPI()

origins = ["https://localhost:8080"]

db = TinyDB("db.json")
repository = get_repository(db=db)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(get_router(repository))
