from app.langgraph.state import ChatState
from app.integrations.langchain.chat_model import (
    LangChainChatModel,
)


class ChatNode:

    def __init__(self):

        self.model = LangChainChatModel()

    async def __call__(
        self,
        state: ChatState,
    ):

        response = await self.model.model.ainvoke(
            state["messages"],
        )

        return {
            "messages": [
                response,
            ]
        }