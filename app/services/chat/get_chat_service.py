from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.chat_repository import ChatRepository


class GetChatService:

    def __init__(self):
        self.chat_repository = ChatRepository()

    def execute(
        self,
        db: Session,
        current_user: User,
        chat_id: int,
    ):
        chat = self.chat_repository.get_by_id(
            db=db,
            chat_id=chat_id,
            user_id=current_user.id,
        )

        if chat is None:
            raise HTTPException(
                status_code=404,
                detail="Chat not found.",
            )

        return chat