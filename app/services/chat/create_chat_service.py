from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.chat_repository import ChatRepository
from app.schemas.chat import ChatCreate


class CreateChatService:

    def __init__(self):
        self.chat_repository = ChatRepository()

    def execute(
        self,
        db: Session,
        current_user: User,
        chat: ChatCreate,
    ):
        return self.chat_repository.create(
            db=db,
            user_id=current_user.id,
            title=chat.title,
        )