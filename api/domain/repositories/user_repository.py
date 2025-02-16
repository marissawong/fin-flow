from abc import ABC, abstractmethod

from pydantic import EmailStr

from domain.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User):
        pass    # TODO: Add

    @abstractmethod
    def get_by_email(self, email: EmailStr):
        pass    # TODO: Add
