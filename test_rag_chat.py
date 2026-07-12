import asyncio

from app.services.rag.rag_chat_service import (
    RAGChatService,
)


async def main():

    service = RAGChatService()

    answer = await service.execute(
        "What technologies does Jubayer know?"
    )

    print(answer)


asyncio.run(main())