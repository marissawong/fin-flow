from application.dto.user_dto import UserDTO
from domain.entities.user import User
from domain.repositories.user_repository import UserRepository


class CreateUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_dto: UserDTO) -> User:
        user = User.create(user_dto.name, user_dto.email)
        self.user_repository.save(user)
        return user