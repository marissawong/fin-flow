from pydantic import EmailStr

from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository


class CreateUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, name: str, email: EmailStr) -> User:
        user = User.create_user(name, email)
        return self.user_repository.create(user)