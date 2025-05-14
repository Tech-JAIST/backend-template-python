from fastapi import APIRouter

from backend.repository import Repository
from .ping import get_ping_router
from .user import get_user_router


def get_router(repository: Repository) -> APIRouter:
    """Create a router for the application.

    Returns:
        APIRouter: The main router for the application.

    """
    router = APIRouter()

    router.include_router(get_ping_router(repository))
    router.include_router(get_user_router(repository))

    return router


__all__ = ["get_router"]
