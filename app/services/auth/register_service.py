from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.models.user import User


class RegisterService:
    def __init__(self):
        self.user_repository = UserRepository()

    def execute(
        self,
        db: Session,
        user: UserCreate,
    ) -> User:

        existing_user = self.user_repository.get_by_email(
            db=db,
            email=user.email,
        )

        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="Email already registered.",
            )

        return self.user_repository.create(
            db=db,
            username=user.username,
            email=user.email,
            hashed_password=hash_password(user.password),
        )