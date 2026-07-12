from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.document import Document


class DocumentRepository:

    def create(
        self,
        *,
        user_id: int,
        original_filename: str,
        stored_filename: str,
        file_type: str,
    ) -> Document:

        return Document(
            user_id=user_id,
            original_filename=original_filename,
            stored_filename=stored_filename,
            file_type=file_type,
        )

    def get_by_id(
        self,
        db: Session,
        document_id: int,
    ) -> Document | None:

        statement = (
            select(Document)
            .where(Document.id == document_id)
        )

        result = db.execute(statement)

        return result.scalar_one_or_none()

    def list_by_user(
        self,
        db: Session,
        user_id: int,
    ) -> list[Document]:

        statement = (
            select(Document)
            .where(Document.user_id == user_id)
            .order_by(Document.created_at.desc())
        )

        result = db.execute(statement)

        return list(result.scalars().all())