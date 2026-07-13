from app.services.rag.search_documents_service import (
    SearchDocumentsService,
)


class RetrievalService:

    def __init__(self):

        self.search_service = (
            SearchDocumentsService()
        )

    def execute(
        self,
        question: str,
    ) -> str:

        chunks = self.search_service.execute(
            question=question,
        )

        if not chunks:

            return (
                "No relevant documents found."
            )

        return "\n\n".join(

            chunk.content

            for chunk in chunks

        )