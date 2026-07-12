import httpx

from app.integrations.llm.base import BaseLLMClient
from app.core.settings import settings
from app.schemas.ai import ChatMessage

class OllamaClient(BaseLLMClient):

    async def generate(
        self,
        messages: list[ChatMessage],
    ) -> str:

        async with httpx.AsyncClient(
            timeout=settings.OLLAMA_TIMEOUT,
        ) as client:

            response = await client.post(
                f"{settings.OLLAMA_BASE_URL}/api/chat",
                json={
                    "model": settings.OLLAMA_MODEL,
                    "messages": [
                        message.model_dump()
                        for message in messages
                    ],
                    "stream": False,
                },
            )

            response.raise_for_status()

            data = response.json()

            return data["message"]["content"]