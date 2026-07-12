from sqlalchemy.orm import Session

from app.services.ai.conversation_service import ConversationService
from app.services.ai.generate_response_service import GenerateResponseService


class ChatService:

    def __init__(self):
        self.conversation_service = ConversationService()
        self.generate_response_service = GenerateResponseService()

    async def execute(
        self,
        db: Session,
        chat_id: int,
    ) -> str:
        # Load the complete conversation
        messages = self.conversation_service.execute(
            db=db,
            chat_id=chat_id,
        )

        # Generate the assistant response
        return await self.generate_response_service.execute(
            messages=messages,
        )