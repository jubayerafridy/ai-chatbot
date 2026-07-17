from app.integrations.langchain.chat_model import (
    LangChainChatModel,
)
from app.langgraph.state import (
    ChatState,
)
from app.prompts.manager import (
    prompt_manager,
)


class ChatNode:

    async def __call__(
        self,
        state: ChatState,
    ):

        model = LangChainChatModel()

        messages = (
            prompt_manager.build_messages(
                state["messages"],
            )
        )

        response = await model.invoke(
            messages,
        )

        return {
            "messages": [
                response,
            ]
        }