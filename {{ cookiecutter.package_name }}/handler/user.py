from fastapi import APIRouter
from pydantic import BaseModel

from ..repository import Repository


class User(BaseModel):
    id: str
    name: str


class UserResponse(BaseModel):
    users: list[User]


def get_user_router(repository: Repository) -> APIRouter:
    """Create a router for the user endpoint.

    Returns:
        APIRouter: The router for the user endpoint.

    """
    router = APIRouter(prefix="/user", tags=["user"])

    @router.get("")
    async def get_users() -> UserResponse:
        users = repository.user_repository.get_users()
        user_responses = [User(id=user.id, name=user.name) for user in users]
        return UserResponse(users=user_responses)

    return router


__all__ = ["get_user_router"]
