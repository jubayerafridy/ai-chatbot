class PromptInjectionValidator:

    BLOCKED_PATTERNS = [

        "ignore previous",

    "ignore all previous",

    "forget previous",

    "forget all previous",

    "reveal system",

    "show system",

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