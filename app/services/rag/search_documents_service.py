from app.rag.embeddings.sentence_transformer_service import (
    SentenceTransformerEmbeddingService,
)
from app.rag.vectorstores.qdrant_service import (
    QdrantVectorStore,
)
from app.schemas.rag import RetrievedChunk


class SearchDocumentsService:

    def __init__(self):

        self.embedding_service = (
            SentenceTransformerEmbeddingService()
        )

        self.vector_store = (
            QdrantVectorStore()
        )

    def execute(
        self,
        question: str,
        limit: int = 5,
        document_ids: list[int] | None = None,
    ) -> list[RetrievedChunk]:

        vector = self.embedding_service.embed(
            question,
        )

        results = self.vector_store.search(
            vector=vector,
            limit=limit,
            document_ids=document_ids,
        )

        chunks: list[RetrievedChunk] = []

        for point in results:

            chunks.append(
                RetrievedChunk(
                    document_id=point.payload["document_id"],
                    chunk_index=point.payload["chunk_index"],
                    content=point.payload["content"],
                    score=point.score,
                )
            )

        return chunks