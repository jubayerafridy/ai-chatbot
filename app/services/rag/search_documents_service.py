from app.rag.embeddings.sentence_transformer_service import (
    SentenceTransformerEmbeddingService,
)
from app.rag.vectorstores.qdrant_service import (
    QdrantVectorStore,
)


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
    ):

        vector = self.embedding_service.embed(
            question,
        )

        return self.vector_store.search(
            vector=vector,
            limit=limit,
        )