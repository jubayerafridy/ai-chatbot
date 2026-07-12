from app.services.rag.search_documents_service import (
    SearchDocumentsService,
)

service = SearchDocumentsService()

results = service.execute(
    "What experience does Jubayer have with FastAPI?"
)

print(f"Found {len(results)} results\n")

for result in results:

    print("=" * 60)

    print(result.score)

    print()

    print(
        result.payload["content"][:300]
    )

    print()