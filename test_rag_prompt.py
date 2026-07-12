from app.rag.prompt.rag_prompt_builder import (
    RAGPromptBuilder,
)
from app.services.rag.search_documents_service import (
    SearchDocumentsService,
)

search = SearchDocumentsService()

results = search.execute(
    "What experience does Jubayer have with FastAPI?"
)

builder = RAGPromptBuilder()

prompt = builder.build(
    question="What experience does Jubayer have with FastAPI?",
    results=results,
)

print(prompt)