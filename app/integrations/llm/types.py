from dataclasses import dataclass


@dataclass
class LLMResponse:

    content: str

    model: str

    provider: str