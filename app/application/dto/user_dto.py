import uuid

from pydantic import BaseModel, EmailStr


class UserDTO(BaseModel):
    user_id: uuid.UUID
    name: str
    email: EmailStr

    class Config:
        from_attributes = True  # SQLAlchemy -> Pydantic