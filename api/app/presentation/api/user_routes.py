from http.client import HTTPException

from fastapi import APIRouter, Depends
from pydantic import EmailStr
from sqlalchemy.orm import Session

from app.application.dto.user_dto import UserDTO
from app.application.use_cases.create_user import CreateUser
from app.application.use_cases.get_user import GetUserByEmail
from app.infrastructure.database import get_db
from app.infrastructure.repositories.user_repository_impl import UserRepositoryImpl

router = APIRouter(prefix="/user", tags=["Users"])

@router.get("/{email}")
def get_user(email: EmailStr, db: Session = Depends(get_db)):
    user_repo = UserRepositoryImpl(db)
    use_case = GetUserByEmail(user_repo)
    user = use_case.execute(email)

    if not user:
        raise HTTPException()

    return UserDTO.model_validate(user)

@router.post("/")
def create_user(name: str, email: EmailStr, db: Session = Depends(get_db)):
    user_repo = UserRepositoryImpl(db)
    use_case = CreateUser(user_repo)
    return use_case.execute(name, email)
