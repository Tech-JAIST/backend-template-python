from pydantic import BaseModel
from tinydb import Query, TinyDB

from backend.domain import User


class UserRepository(BaseModel):
    db: TinyDB

    def __init__(self, db: TinyDB) -> None:
        """Initialize the user repository.

        Args:
            db (TinyDB): The database.

        """
        self.db = db

    def get_users(self) -> list[User]:
        """Get all users.

        Returns:
            list: The list of users.

        """
        user = Query()
        users = self.db.search(user.name.exists())
        return [User(**user) for user in users]


def get_user_repository(db: TinyDB) -> UserRepository:
    """Get the user repository.

    Returns:
        UserRepository: The user repository.

    """
    return UserRepository(db=db)


__all__ = ["get_user_repository"]
