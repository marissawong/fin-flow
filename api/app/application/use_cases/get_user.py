from pydantic import EmailStr

from app.domain.repositories.user_repository import UserRepository


class GetUserByEmail:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, email: EmailStr):
        return self.user_repository.get(email)