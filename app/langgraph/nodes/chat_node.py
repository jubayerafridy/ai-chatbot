from app.integrations.langchain.chat_model import (
    LangChainChatModel,
)
from app.langgraph.state import (
    ChatState,
)


class ChatNode:

    async def __call__(
        self,
        state: ChatState,
    ):

        model = LangChainChatModel()

        response = await model.invoke(
            state["messages"],
        )


        return {
            "messages": [
                response,
            ]
        }