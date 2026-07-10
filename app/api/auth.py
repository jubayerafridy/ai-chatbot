from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.auth import LoginRequest, TokenResponse
from app.schemas.user import UserCreate, UserResponse
from app.services.auth.login_service import LoginService
from app.services.auth.register_service import RegisterService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

register_service = RegisterService()
login_service = LoginService()


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201,
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    return register_service.execute(
        db=db,
        user=user,
    )


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    credentials: LoginRequest,
    db: Session = Depends(get_db),
):
    return login_service.execute(
        db=db,
        credentials=credentials,
    )