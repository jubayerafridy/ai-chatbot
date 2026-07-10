from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.db.session import get_db
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

user_repository = UserRepository()


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201,
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    # Check if email already exists
    existing_user = user_repository.get_by_email(
        db=db,
        email=user.email,
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered.",
        )

    # Create the user
    new_user = user_repository.create(
        db=db,
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password),
    )

    return new_user