from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.document_chunk import DocumentChunk


class DocumentChunkRepository:

    def create(
        self,
        *,
        document_id: int,
        chunk_index: int,
        content: str,
    ) -> DocumentChunk:

        return DocumentChunk(
            document_id=document_id,
            chunk_index=chunk_index,
            content=content,
        )

    def list_by_document(
        self,
        db: Session,
        document_id: int,
    ) -> list[DocumentChunk]:

        statement = (
            select(DocumentChunk)
            .where(DocumentChunk.document_id == document_id)
            .order_by(DocumentChunk.chunk_index.asc())
        )

        result = db.execute(statement)

        return list(result.scalars().all())