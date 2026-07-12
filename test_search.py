from app.services.rag.search_documents_service import (
    SearchDocumentsService,
)

service = SearchDocumentsService()

results = service.execute(
    question="What technologies does Jubayer know?",
    document_ids=[36],   # your current document id
)

print(f"Found {len(results)} results\n")

for result in results:

    print("=" * 60)
    print(result.score)
    print()
    print(result.content[:300])
    print()