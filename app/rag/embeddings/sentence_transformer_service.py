from sentence_transformers import SentenceTransformer

from app.rag.embeddings.base import (
    BaseEmbeddingService,
)


class SentenceTransformerEmbeddingService(
    BaseEmbeddingService,
):

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def embed(
        self,
        text: str,
    ) -> list[float]:

        embedding = self.model.encode(
            text,
            normalize_embeddings=True,
        )

        return embedding.tolist()