from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.chat_repository import ChatRepository


class ListChatsService:

    def __init__(self):
        self.chat_repository = ChatRepository()

    def execute(
        self,
        db: Session,
        current_user: User,
    ):
        return self.chat_repository.get_all_by_user(
            db=db,
            user_id=current_user.id,
        )