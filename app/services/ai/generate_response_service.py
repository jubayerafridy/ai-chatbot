import httpx
from fastapi import HTTPException

from app.integrations.langchain.chat_model import (
    LangChainChatModel,
)
from app.models.message import Message
from app.prompt.prompt_builder import PromptBuilder


class GenerateResponseService:

    def __init__(self):

        self.client = (
            LangChainChatModel()
        )

        self.builder = (
            PromptBuilder()
        )

    async def execute(
        self,
        messages: list[Message],
        context: str | None = None,
    ) -> str:

        chat_messages = self.builder.build(
            messages=messages,
            context=context,
        )

        try:

            return await self.client.generate(
                messages=chat_messages,
            )

        except httpx.ConnectError:

            raise HTTPException(
                status_code=503,
                detail="AI service is unavailable.",
            )

        except httpx.TimeoutException:

            raise HTTPException(
                status_code=504,
                detail="AI service timed out.",
            )

        except httpx.HTTPStatusError as exc:

            raise HTTPException(
                status_code=502,
                detail=(
                    f"AI provider returned HTTP "
                    f"{exc.response.status_code}."
                ),
            )