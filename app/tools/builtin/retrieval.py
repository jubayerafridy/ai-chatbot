from app.services.rag.search_documents_service import (
    SearchDocumentsService,
)
from app.tools.base.tool import BaseTool


class RetrievalTool(BaseTool):

    def __init__(self):

        self.search = (
            SearchDocumentsService()
        )

    @property
    def name(self) -> str:

        return "retrieve_documents"

    @property
    def description(self) -> str:

        return (
            "Search uploaded documents for information "
            "relevant to a user question."
        )

    async def execute(
        self,
        question: str,
    ) -> str:

        chunks = self.search.execute(
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