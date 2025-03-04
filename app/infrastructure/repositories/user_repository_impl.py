from pydantic import EmailStr
from sqlalchemy.orm import Session

from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository


class UserRepositoryImpl(UserRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get(self, email: EmailStr):
        return self.db.query(User).filter(User.email == email).first()

    def delete(self, email: EmailStr):
        return self.db.query(User).filter(User.email == email).delete()