from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.chat import Chat


class ChatRepository:

    def create(
        self,
        db: Session,
        user_id: int,
        title: str = "New Chat",
    ) -> Chat:

        chat = Chat(
            user_id=user_id,
            title=title,
        )

        db.add(chat)
        db.commit()
        db.refresh(chat)

        return chat

    def get_all_by_user(
        self,
        db: Session,
        user_id: int,
    ) -> list[Chat]:

        statement = (
            select(Chat)
            .where(Chat.user_id == user_id)
            .order_by(Chat.created_at.desc())
        )

        result = db.execute(statement)

        return list(result.scalars().all())
    
    def get_by_id(
    self,
    db: Session,
    chat_id: int,
    user_id: int,
) -> Chat | None:

        statement = (
            select(Chat)
            .where(
                Chat.id == chat_id,
                Chat.user_id == user_id,
            )
        )

        result = db.execute(statement)

        return result.scalar_one_or_none()
    
    def update_title(
        self,
        chat: Chat,
        title: str,
    ) -> Chat:

        chat.title = title

        return chat