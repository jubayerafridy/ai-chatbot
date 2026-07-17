from langchain_core.messages import (
    BaseMessage,
    SystemMessage,
)

from app.prompts.templates import (
    SYSTEM_PROMPT,
)


class PromptManager:

    def build_messages(
        self,
        messages: list[BaseMessage],
    ) -> list[BaseMessage]:

        return [
            SystemMessage(
                content=SYSTEM_PROMPT,
            ),
            *messages,
        ]


prompt_manager = PromptManager()