from app.services.rag.search_documents_service import (
    SearchDocumentsService,
)


class RetrievalService:

    def __init__(self):

        self.search_service = (
            SearchDocumentsService()
        )

    # def execute(
    #     self,
    #     question: str,
    # ) -> str:

    #     chunks = self.search_service.execute(
    #         question=question,
    #     )

    #     if not chunks:

    #         return (
    #             "No relevant documents found."
    #         )

    #     return "\n\n".join(

    #         chunk.content

    #         for chunk in chunks

    #     )
    
    def execute(
        self,
        question: str,
    ) -> str:

        print("=" * 60)
        print("QUESTION:", question)

        chunks = self.search_service.execute(
            question=question,
        )

        print("CHUNKS FOUND:", len(chunks))

        for chunk in chunks:
            print(chunk.content)

        print("=" * 60)

        if not chunks:
            return "No relevant documents found."

        return "\n\n".join(
            chunk.content
            for chunk in chunks
        )