from fastapi import HTTPException
import httpx

from app.models.message import Message
from app.prompt.prompt_builder import PromptBuilder
from app.services.ai.langgraph_service import (
    LangGraphService,
)


class GenerateResponseService:

    def __init__(self):

        self.graph = LangGraphService()

        self.builder = PromptBuilder()

    async def execute(
        self,
        messages: list[Message],
        thread_id: str,
        context: str | None = None,
    ) -> str:

        if not messages:
            raise HTTPException(
                status_code=400,
                detail="Conversation is empty.",
            )

        try:

            prompt = self.builder.build(
                messages=messages,
                context=context,
            )

            return await self.graph.execute(
                message=prompt[-1].content,
                thread_id=thread_id,
            )

        except httpx.ConnectError:

            raise HTTPException(
                status_code=503,
                detail="AI service unavailable.",
            )

        except httpx.TimeoutException:

            raise HTTPException(
                status_code=504,
                detail="AI service timeout.",
            )

        except httpx.HTTPStatusError as exc:

            raise HTTPException(
                status_code=502,
                detail=f"AI provider returned HTTP {exc.response.status_code}.",
            )