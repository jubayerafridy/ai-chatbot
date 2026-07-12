from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.message import MessageRole
from app.models.user import User
from app.repositories.chat_repository import ChatRepository
from app.repositories.message_repository import MessageRepository
from app.schemas.message import (
    MessageCreate,
    SendMessageResponse,
)
from app.services.ai.conversation_service import ConversationService
from app.services.ai.generate_response_service import (
    GenerateResponseService,
)
from app.services.rag.search_documents_service import (
    SearchDocumentsService,
)


class SendMessageService:

    def __init__(self):
        self.chat_repository = ChatRepository()
        self.message_repository = MessageRepository()

        self.conversation_service = ConversationService()
        self.generate_response_service = GenerateResponseService()
        self.search_documents_service = (
            SearchDocumentsService()
        )

    async def execute(
        self,
        db: Session,
        current_user: User,
        chat_id: int,
        message: MessageCreate,
    ) -> SendMessageResponse:

        # --------------------------
        # Verify chat ownership
        # --------------------------

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

        # --------------------------
        # Update title on first message
        # --------------------------

        if chat.title == "New Chat":

            generated_title = (
                message.content.strip()
            )

            if len(generated_title) > 60:
                generated_title = (
                    generated_title[:57]
                    + "..."
                )

            if not generated_title:
                generated_title = "New Chat"

            self.chat_repository.update_title(
                chat=chat,
                title=generated_title,
            )

        # --------------------------
        # Save USER message
        # --------------------------

        user_message = (
            self.message_repository.create(
                chat_id=chat.id,
                role=MessageRole.USER,
                content=message.content,
            )
        )

        db.add(user_message)

        try:

            db.commit()

            db.refresh(user_message)

        except Exception:

            db.rollback()

            raise

        # --------------------------
        # Load conversation history
        # --------------------------

        messages = (
            self.conversation_service.execute(
                db=db,
                chat_id=chat.id,
            )
        )

        # --------------------------
        # Retrieve relevant documents
        # --------------------------

        retrieved_chunks = (
            self.search_documents_service.execute(
                question=message.content,
            )
        )

        context = None

        if retrieved_chunks:

            context = "\n\n".join(
                (
                    f"[Document {chunk.document_id}"
                    f" | Chunk {chunk.chunk_index}]\n"
                    f"{chunk.content}"
                )
                for chunk in retrieved_chunks
            )

        # --------------------------
        # Generate AI response
        # --------------------------

        assistant_text = (
            await self.generate_response_service.execute(
                messages=messages,
                context=context,
            )
        )

        # --------------------------
        # Save assistant message
        # --------------------------

        assistant_message = (
            self.message_repository.create(
                chat_id=chat.id,
                role=MessageRole.ASSISTANT,
                content=assistant_text,
            )
        )

        db.add(assistant_message)

        try:

            db.commit()

            db.refresh(
                assistant_message,
            )

        except Exception:

            db.rollback()

            raise

        return SendMessageResponse(
            user=user_message,
            assistant=assistant_message,
        )