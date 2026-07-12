from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.chat import ChatCreate, ChatResponse
from app.services.chat.create_chat_service import CreateChatService
from app.services.chat.list_chats_service import ListChatsService
from app.services.chat.get_chat_service import GetChatService
from app.schemas.message import (
    MessageCreate,
    MessageResponse,
    SendMessageResponse,
)
from app.services.chat.send_message_service import SendMessageService
from app.services.chat.list_messages_service import ListMessagesService
from app.schemas.message import MessageResponse


router = APIRouter(
    prefix="/chats",
    tags=["Chats"],
)

create_chat_service = CreateChatService()
list_chats_service = ListChatsService()
get_chat_service = GetChatService()
send_message_service = SendMessageService()
list_messages_service = ListMessagesService()


@router.post(
    "",
    response_model=ChatResponse,
    status_code=201,
)
def create_chat(
    chat: ChatCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_chat_service.execute(
        db=db,
        current_user=current_user,
        chat=chat,
    )

@router.get(
    "",
    response_model=list[ChatResponse],
)
def list_chats(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return list_chats_service.execute(
        db=db,
        current_user=current_user,
    )

@router.get(
    "/{chat_id}",
    response_model=ChatResponse,
)
def get_chat(
    chat_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_chat_service.execute(
        db=db,
        current_user=current_user,
        chat_id=chat_id,
    )

@router.post(
    "/{chat_id}/messages",
    response_model=SendMessageResponse,
    status_code=201,
)
async def send_message(
    chat_id: int,
    message: MessageCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await send_message_service.execute(
        db=db,
        current_user=current_user,
        chat_id=chat_id,
        message=message,
    )

@router.get(
    "/{chat_id}/messages",
    response_model=list[MessageResponse],
)
def list_messages(
    chat_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return list_messages_service.execute(
        db=db,
        current_user=current_user,
        chat_id=chat_id,
    )