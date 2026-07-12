from fastapi import APIRouter
from app.schemas.ai import ChatMessage

from app.integrations.llm.ollama_client import OllamaClient
from app.schemas.llm import (
    PromptRequest,
    PromptResponse,
)

router = APIRouter(
    prefix="/llm",
    tags=["LLM"],
)

client = OllamaClient()


@router.post(
    "/test",
    response_model=PromptResponse,
)
async def test_llm(
    request: PromptRequest,
):
    response = await client.generate(
    messages=[
        ChatMessage(
            role="user",
            content=request.prompt,
        )
    ],
)

    return PromptResponse(
        response=response,
    )