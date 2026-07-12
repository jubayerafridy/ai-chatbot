from app.rag.prompt.rag_prompt_builder import (
    RAGPromptBuilder,
)
from app.rag.embeddings.sentence_transformer_service import (
    SentenceTransformerEmbeddingService,
)
from app.rag.vectorstores.qdrant_service import (
    QdrantVectorStore,
)
from app.integrations.llm.ollama_client import (
    OllamaClient,
)
from app.schemas.ai import ChatMessage


class RAGChatService:

    def __init__(self):

        self.embedding_service = (
            SentenceTransformerEmbeddingService()
        )

        self.vector_store = (
            QdrantVectorStore()
        )

        self.prompt_builder = (
            RAGPromptBuilder()
        )

        self.client = (
            OllamaClient()
        )

    async def execute(
        self,
        question: str,
    ) -> str:

        vector = self.embedding_service.embed(
            question,
        )

        results = self.vector_store.search(
            vector=vector,
            limit=5,
        )

        prompt = self.prompt_builder.build(
            question=question,
            results=results,
        )

        messages = [
            ChatMessage(
                role="user",
                content=prompt,
            )
        ]

        return await self.client.generate(
            messages=messages,
        )