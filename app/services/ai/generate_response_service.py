from app.integrations.llm.ollama_client import OllamaClient
from app.models.message import Message
from app.prompt.prompt_builder import PromptBuilder


class GenerateResponseService:

    def __init__(self):
        self.client = OllamaClient()
        self.builder = PromptBuilder()

    async def execute(
        self,
        messages: list[Message],
    ) -> str:
        # Build structured chat messages
        chat_messages = self.builder.build(
            messages,
        )

        # Send them to the LLM
        return await self.client.generate(
            messages=chat_messages,
        )