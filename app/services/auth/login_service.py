from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.jwt import create_access_token
from app.core.security import verify_password
from app.repositories.user_repository import UserRepository
from app.schemas.auth import LoginRequest, TokenResponse


class LoginService:
    def __init__(self):
        self.user_repository = UserRepository()

    def execute(
        self,
        db: Session,
        credentials: LoginRequest,
    ) -> TokenResponse:

        user = self.user_repository.get_by_email(
            db=db,
            email=credentials.email,
        )

        if (
            user is None
            or not verify_password(
                credentials.password,
                user.hashed_password,
            )
        ):
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password.",
            )

        access_token = create_access_token(
            data={
                "sub": str(user.id),
            }
        )

        return TokenResponse(
            access_token=access_token,
        )