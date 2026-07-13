from langchain_core.messages import BaseMessage
from langchain_ollama import ChatOllama

from app.core.settings import settings
from app.tools.registry import (
    ToolRegistry,
)


class LangChainChatModel:

    def __init__(self):

        registry = ToolRegistry()

        tools = registry.list()


        self.model = ChatOllama(
            model=settings.OLLAMA_MODEL,
            base_url=settings.OLLAMA_BASE_URL,
            temperature=0,
        ).bind_tools(
            tools,
        )

    async def invoke(
        self,
        messages: list[BaseMessage],
    ):

        return await self.model.ainvoke(
            messages,
        )