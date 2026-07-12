from sqlalchemy.orm import Session

from app.models.message import Message
from app.repositories.message_repository import MessageRepository
from app.core.settings import settings

class ConversationService:

    def __init__(self):
        self.message_repository = MessageRepository()

    def execute(
        self,
        db: Session,
        chat_id: int,
    ) -> list[Message]:

        messages = self.message_repository.get_by_chat(
        db=db,
        chat_id=chat_id,
    )

        return messages[-settings.MAX_HISTORY_MESSAGES:]