from app.models.message import Message, MessageRole
from sqlalchemy import select
from sqlalchemy.orm import Session

class MessageRepository:

    def create(
        self,
        chat_id: int,
        role: MessageRole,
        content: str,
    ) -> Message:

        return Message(
            chat_id=chat_id,
            role=role,
            content=content,
        )
    
    def get_by_chat(
        self,
        db: Session,
        chat_id: int,
    ) -> list[Message]:

        statement = (
            select(Message)
            .where(Message.chat_id == chat_id)
            .order_by(Message.created_at.asc())
        )

        result = db.execute(statement)

        return list(result.scalars().all())