from fastapi import APIRouter
from pydantic import BaseModel

from backend.repository import Repository


class PingResponse(BaseModel):
    message: str


def get_ping_router(repoository: Repository) -> APIRouter:
    """Create a router for the ping endpoint.

    Returns:
        APIRouter: The router for the ping endpoint.

    """
    router = APIRouter(prefix="/ping", tags=["ping"])

    @router.get("")
    async def ping() -> PingResponse:
        return PingResponse(message="pong")

    return router


__all__ = ["get_ping_router"]
