from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)
from langchain_ollama import ChatOllama

from app.core.settings import settings
from app.schemas.ai import ChatMessage


class LangChainChatModel:

    def __init__(self):

        self.model = ChatOllama(
            model=settings.OLLAMA_MODEL,
            base_url=settings.OLLAMA_BASE_URL,
            temperature=0,
        )

    async def generate(
        self,
        messages: list[ChatMessage],
    ) -> str:

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

        return response.content