from app.models.message import Message
from app.schemas.ai import ChatMessage


class PromptBuilder:

    BASE_SYSTEM_PROMPT = """
You are a Retrieval-Augmented Generation (RAG) AI assistant.

Your responsibilities:

- Answer ONLY using the retrieved context provided below.
- Do NOT use your own knowledge if the answer is missing.
- Do NOT guess or invent information.
- Do NOT mix retrieved context with outside knowledge.
- If the answer is not explicitly contained in the retrieved context,
  respond exactly with:

"I don't have enough information in the uploaded documents."

If no retrieved context is provided, answer normally as a helpful AI assistant.
""".strip()

    def build_system_prompt(
        self,
        context: str | None,
    ) -> str:

        if not context:

            return self.BASE_SYSTEM_PROMPT

        return (
            f"{self.BASE_SYSTEM_PROMPT}\n\n"
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