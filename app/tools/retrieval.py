from langchain_core.tools import tool

from app.services.tools.retrieval_service import (
    RetrievalService,
)


retrieval_service = (
    RetrievalService()
)


@tool
async def retrieve_documents(
    question: str,
) -> str:
    """
    Search uploaded documents for information
    relevant to the user's question.
    """

    return retrieval_service.execute(
        question,
    )