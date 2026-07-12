from app.models.message import Message
from app.prompt.base.system_prompt import (
    BASE_SYSTEM_PROMPT,
)
from app.schemas.ai import ChatMessage


class PromptBuilder:

    def build_system_prompt(
        self,
        context: str | None,
    ) -> str:

        if not context:

            return BASE_SYSTEM_PROMPT

        return (
            f"{BASE_SYSTEM_PROMPT}\n\n"
            "==============================\n"
            "RETRIEVED CONTEXT\n"
            "==============================\n\n"
            f"{context}\n\n"
            "==============================\n"
            "END OF CONTEXT\n"
            "=============================="
        )

    def build(
        self,
        messages: list[Message],
        context: str | None = None,
    ) -> list[ChatMessage]:

        prompt = [
            ChatMessage(
                role="system",
                content=self.build_system_prompt(
                    context=context,
                ),
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