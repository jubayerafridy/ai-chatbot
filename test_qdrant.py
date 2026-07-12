from app.rag.vectorstores.qdrant_service import (
    QdrantVectorStore,
)

store = QdrantVectorStore()

store.create_collection()

print("Collection created successfully!")