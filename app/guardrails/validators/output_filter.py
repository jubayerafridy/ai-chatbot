class OutputFilterValidator:

    BLOCKED_PATTERNS = [

        "BEGIN PRIVATE KEY",

        "OPENAI_API_KEY",

        "DATABASE_URL",

    ]

    def validate(
        self,
        text: str,
    ) -> None:

        lowered = text.lower()

        for pattern in self.BLOCKED_PATTERNS:

            if pattern.lower() in lowered:

                raise ValueError(
                    "Sensitive output detected."
                )