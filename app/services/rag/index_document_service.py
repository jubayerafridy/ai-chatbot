from sqlalchemy.orm import Session

from app.repositories.document_chunk_repository import (
    DocumentChunkRepository,
)
from app.rag.embeddings.sentence_transformer_service import (
    SentenceTransformerEmbeddingService,
)
from app.rag.vectorstores.qdrant_service import (
    QdrantVectorStore,
)


class IndexDocumentService:

    def __init__(self):

        self.chunk_repository = (
            DocumentChunkRepository()
        )

        self.embedding_service = (
            SentenceTransformerEmbeddingService()
        )

        self.vector_store = (
            QdrantVectorStore()
        )

    def execute(
        self,
        db: Session,
        document_id: int,
    ) -> None:

        chunks = (
            self.chunk_repository.get_by_document(
                db=db,
                document_id=document_id,
            )
        )

        ids = []

        vectors = []

        payloads = []

        for chunk in chunks:

            vector = (
                self.embedding_service.embed(
                    chunk.content,
                )
            )

            ids.append(
                chunk.id
            )

            vectors.append(
                vector
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