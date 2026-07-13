from app.models.document_chunk import (
    DocumentChunk,
)
from app.rag.embeddings.sentence_transformer_service import (
    SentenceTransformerEmbeddingService,
)
from app.rag.vectorstores.qdrant_service import (
    QdrantVectorStore,
)


class VectorIndexService:

    def __init__(self):

        self.embedding_service = (
            SentenceTransformerEmbeddingService()
        )

        self.vector_store = (
            QdrantVectorStore()
        )

    def index_chunks(
        self,
        chunks: list[DocumentChunk],
    ) -> None:

        if not chunks:
            return

        self.vector_store.create_collection()

        ids: list[int] = []

        vectors: list[list[float]] = []

        payloads: list[dict] = []

        for chunk in chunks:

            embedding = (
                self.embedding_service.embed(
                    chunk.content,
                )
            )

            ids.append(
                chunk.id,
            )

            vectors.append(
                embedding,
            )

            payloads.append(
                {
                    "document_id": chunk.document_id,
                    "chunk_index": chunk.chunk_index,
                    "content": chunk.content,
                }
            )

        self.vector_store.upsert(
            ids=ids,
            vectors=vectors,
            payloads=payloads,
        )