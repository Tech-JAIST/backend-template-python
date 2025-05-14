from pydantic import BaseModel
from tinydb import TinyDB

from .user import UserRepository, get_user_repository


class Repository(BaseModel):
    user_repository: UserRepository


def get_repository(db: TinyDB) -> Repository:
    """Get the repository.

    Returns:
        Repository: repository.

    """
    user_repository = get_user_repository(db=db)
    return Repository(user_repository=user_repository)


__all__ = ["get_repository"]
