from app.models.document_chunk import DocumentChunk
from app.rag.embeddings.sentence_transformer_service import (
    SentenceTransformerEmbeddingService,
)


class GenerateEmbeddingsService:

    def __init__(self):

        self.embedding_service = (
            SentenceTransformerEmbeddingService()
        )

    def execute(
        self,
        chunks: list[DocumentChunk],
    ) -> list[list[float]]:

        embeddings = []

        for chunk in chunks:

            vector = (
                self.embedding_service.embed(
                    chunk.content,
                )
            )

            embeddings.append(vector)

        return embeddings