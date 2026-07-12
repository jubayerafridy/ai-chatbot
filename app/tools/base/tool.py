from abc import ABC, abstractmethod
from typing import Any


class BaseTool(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Unique tool name.
        """
        ...

    @property
    @abstractmethod
    def description(self) -> str:
        """
        Description shown to the LLM.
        """
        ...

    @abstractmethod
    async def execute(
        self,
        **kwargs: Any,
    ) -> Any:
        """
        Execute the tool.
        """
        ...