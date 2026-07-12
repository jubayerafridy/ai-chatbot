from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.document import Document
from app.services.rag.process_document_service import (
    ProcessDocumentService,
)

db: Session = SessionLocal()

document = db.get(
    Document,
    2,   # Change this if your document ID is different
)

if document is None:
    raise Exception("Document not found.")

service = ProcessDocumentService()

service.execute(
    db=db,
    document=document,
)

print("Document processed successfully!")

db.close()