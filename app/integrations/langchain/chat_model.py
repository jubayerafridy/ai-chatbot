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
from app.schemas.tool_call import ToolCall
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
        ).bind_tools(
            tools,
        )

    async def generate(
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

        response = await self.model.ainvoke(
            langchain_messages,
        )

        if response.tool_calls:

            tool_calls = []

            for tool in response.tool_calls:

                tool_calls.append(
                    ToolCall(
                        id=tool["id"],
                        name=tool["name"],
                        arguments=tool["args"],
                    )
                )

            return tool_calls

        return response.content