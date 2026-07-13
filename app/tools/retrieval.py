from langchain_core.tools import tool

from app.services.tools.retrieval_service import (
    RetrievalService,
)
from app.services.tools.tool_executor import (
    ToolExecutor,
)


retrieval_service = RetrievalService()

tool_executor = ToolExecutor()


@tool
async def retrieve_documents(
    question: str,
) -> str:
    """
    Search uploaded documents for information
    relevant to the user's question.
    """

    return await tool_executor.execute(
        tool_name="retrieve_documents",
        executor=retrieval_service.execute,
        question=question,
    )