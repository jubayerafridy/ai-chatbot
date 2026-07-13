from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)
from langchain_ollama import ChatOllama

from app.core.settings import settings
from app.integrations.langchain.tool_factory import (
    ToolFactory,
)
from app.schemas.ai import ChatMessage
from app.tools.registry import ToolRegistry


class LangChainChatModel:

    def __init__(self):

        registry = ToolRegistry()

        tools = [
            ToolFactory.create(tool)
            for tool in registry.list()
        ]

        self.model = ChatOllama(
            model=settings.OLLAMA_MODEL,
            base_url=settings.OLLAMA_BASE_URL,
            temperature=0,
        ).bind_tools(tools)

    async def invoke(
        self,
        messages: list[ChatMessage],
    ):

        langchain_messages = []

        for message in messages:

            if message.role == "system":

                langchain_messages.append(
                    SystemMessage(
                        content=message.content,
                    )
                )

            elif message.role == "user":

                langchain_messages.append(
                    HumanMessage(
                        content=message.content,
                    )
                )

            else:

                langchain_messages.append(
                    AIMessage(
                        content=message.content,
                    )
                )

        return await self.model.ainvoke(
            langchain_messages,
        )