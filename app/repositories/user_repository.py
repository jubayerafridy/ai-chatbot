from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User
from sqlalchemy.exc import IntegrityError

class UserRepository:

    def get_by_email(
        self,
        db: Session,
        email: str,
    ) -> User | None:
        statement = select(User).where(User.email == email)

        result = db.execute(statement)

        return result.scalar_one_or_none()

    def create(
    self,
    db: Session,
    username: str,
    email: str,
    hashed_password: str,
    ) -> User:

        user = User(
        username=username,
        email=email,
        hashed_password=hashed_password,
        )

        try:
            db.add(user)

            db.commit()

            db.refresh(user)

            return user

        except IntegrityError:
            db.rollback()
            raise