from abc import ABC, abstractmethod

from pydantic import EmailStr

from app.domain.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    def create(self, user: User):
        pass

    @abstractmethod
    def get(self, email: EmailStr):
        pass

    @abstractmethod
    def delete(self, email: EmailStr):
        pass