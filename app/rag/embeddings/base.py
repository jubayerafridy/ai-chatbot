from abc import ABC, abstractmethod


class BaseEmbeddingService(ABC):

    @abstractmethod
    def embed(
        self,
        text: str,
    ) -> list[float]:
        ...