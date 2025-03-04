from http.client import HTTPException

from fastapi import APIRouter, Depends, status, Response
from pydantic import EmailStr
from sqlalchemy.orm import Session

from app.application.dto.create_user_dto import CreateUserDTO
from app.application.dto.user_dto import UserDTO
from app.application.use_cases.create_user import CreateUser
from app.application.use_cases.delete_user import DeleteUser
from app.application.use_cases.get_user import GetUserByEmail
from app.infrastructure.database import get_db
from app.infrastructure.repositories.user_repository_impl import UserRepositoryImpl

router = APIRouter(prefix="/user", tags=["Users"])

@router.get("/{email}")
def get_user(email: EmailStr, response: Response, db: Session = Depends(get_db)):
    user_repo = UserRepositoryImpl(db)
    user = GetUserByEmail(user_repo).execute(email)

    if not user:
        response.status_code = status.HTTP_204_NO_CONTENT
        return "User not found"

    return UserDTO.model_validate(user)

@router.post("/")
def create_user(user: CreateUserDTO, response: Response, db: Session = Depends(get_db)):
    user_repo = UserRepositoryImpl(db)
    user = GetUserByEmail(user_repo).execute(user.email)
    if user:
        response.status_code = status.HTTP_409_CONFLICT
        return f"User with email {user.email} already exists"

    return CreateUser(user_repo).execute(user.name, user.email)

@router.delete("/{email}")
def delete_user(email: EmailStr, response: Response, db: Session = Depends(get_db)):
    user_repo = UserRepositoryImpl(db)
    user = GetUserByEmail(user_repo).execute(email)
    if not user:
        response.status_code = status.HTTP_204_NO_CONTENT
        return "User not found"

    return DeleteUser(user_repo).execute(email)