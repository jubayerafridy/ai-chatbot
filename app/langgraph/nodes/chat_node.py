from app.integrations.langchain.chat_model import (
    LangChainChatModel,
)
from app.langgraph.state import ChatState


class ChatNode:

    def __init__(self):

        self.model = LangChainChatModel()

    async def __call__(
        self,
        state: ChatState,
    ):

        response = await self.model.invoke(
            state["messages"],
        )

        return {
            "messages": [
                response,
            ]
        }