from app.rag.embeddings.sentence_transformer_service import (
    SentenceTransformerEmbeddingService,
)

service = (
    SentenceTransformerEmbeddingService()
)

embedding = service.embed(
    "What is SQLAlchemy?"
)

print(len(embedding))

print(embedding[:10])