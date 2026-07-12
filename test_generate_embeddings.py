from app.db.session import SessionLocal
from app.repositories.document_chunk_repository import (
    DocumentChunkRepository,
)
from app.services.rag.generate_embeddings_service import (
    GenerateEmbeddingsService,
)

db = SessionLocal()

repository = (
    DocumentChunkRepository()
)

chunks = repository.get_by_document(
    db=db,
    document_id=3,
)

service = (
    GenerateEmbeddingsService()
)

vectors = service.execute(
    chunks,
)

print(len(vectors))

print(len(vectors[0]))

db.close()