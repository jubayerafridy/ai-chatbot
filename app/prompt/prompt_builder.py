from app.models.message import Message
from app.schemas.ai import ChatMessage


class PromptBuilder:

    SYSTEM_PROMPT = (
        "You are a helpful AI assistant."
    )

    def build(
        self,
        messages: list[Message],
    ) -> list[ChatMessage]:

        prompt = [
            ChatMessage(
                role="system",
                content=self.SYSTEM_PROMPT,
            )
        ]

        for message in messages:

            prompt.append(
                ChatMessage(
                    role=message.role.value,
                    content=message.content,
                )
            )

        return prompt