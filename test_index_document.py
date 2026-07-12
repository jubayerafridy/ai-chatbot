from app.db.session import SessionLocal
from app.services.rag.index_document_service import (
    IndexDocumentService,
)

db = SessionLocal()

service = IndexDocumentService()

service.execute(
    db=db,
    document_id=36,
)

print("Document indexed successfully!")

db.close()