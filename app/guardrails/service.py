from app.guardrails.validators.prompt_injection import (
    PromptInjectionValidator,
)
from app.guardrails.validators.output_filter import (
    OutputFilterValidator,
)


class GuardrailService:

    def __init__(self):

        self.validators = [

            PromptInjectionValidator(),

        ]
        self.output_validators = [

    OutputFilterValidator(),

]

    def validate_input(
        self,
        text: str,
    ) -> str:

        for validator in self.validators:

            validator.validate(text)

        return text
    def validate_output(
        self,
        text: str,
    ) -> str:

        for validator in self.output_validators:

            validator.validate(text)

        return text