from abc import ABC, abstractmethod


class BaseVectorStore(ABC):

    @abstractmethod
    def create_collection(
        self,
    ) -> None:
        ...

    @abstractmethod
    def upsert(
        self,
        ids: list[int],
        vectors: list[list[float]],
        payloads: list[dict],
    ) -> None:
        ...

    @abstractmethod
    def search(
        self,
        vector: list[float],
        limit: int = 5,
        document_ids: list[int] | None = None,
    ):
        ...