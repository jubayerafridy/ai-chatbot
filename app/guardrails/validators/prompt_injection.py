class PromptInjectionValidator:

    BLOCKED_PATTERNS = [

        "ignore previous instructions",

        "forget previous instructions",

        "reveal system prompt",

        "show system prompt",

        "developer message",

    ]

    def validate(
        self,
        text: str,
    ) -> None:

        lowered = text.lower()

        for pattern in self.BLOCKED_PATTERNS:

            if pattern in lowered:

                raise ValueError(
                    "Prompt injection detected."
                )