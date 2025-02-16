import uuid

from pydantic import EmailStr
from sqlalchemy import Column, UUID, String

from infrastructure.database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    @staticmethod
    def create_user(name: str, email: EmailStr):
        return User(user_id=uuid.uuid4(), name=name, email=email)