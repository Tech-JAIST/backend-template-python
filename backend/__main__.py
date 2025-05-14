import asyncio
from typing import TYPE_CHECKING, cast

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from hypercorn.asyncio import serve
from hypercorn.config import Config
from tinydb import TinyDB

if TYPE_CHECKING:
    from hypercorn.typing import ASGIFramework

from .handler import get_router
from .repository import get_repository


async def run() -> None:
    """Run the FastAPI application.

    This function creates a FastAPI application, sets up CORS middleware,
    """
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

    config = Config()
    config.bind = ["0.0.0.0:8000"]
    await serve(cast("ASGIFramework", app), config)


if __name__ == "__main__":
    asyncio.run(run())
