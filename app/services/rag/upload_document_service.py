from pathlib import Path

from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.models.document import Document
from app.models.user import User
from app.repositories.document_repository import DocumentRepository
from app.services.storage.local_storage_service import (
    LocalStorageService,
)
from app.services.rag.process_document_service import (
    ProcessDocumentService,
)


class UploadDocumentService:

    ALLOWED_EXTENSIONS = {
        ".pdf",
        ".txt",
        ".md",
    }

    def __init__(self):
        self.document_repository = DocumentRepository()
        self.storage_service = LocalStorageService()
        self.process_document_service = (
            ProcessDocumentService()
    )

    def execute(
        self,
        db: Session,
        current_user: User,
        file: UploadFile,
    ) -> Document:

        if file.filename is None:
            raise HTTPException(
                status_code=400,
                detail="Filename is missing.",
            )

        extension = (
            Path(file.filename)
            .suffix
            .lower()
        )

        if extension not in self.ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=400,
                detail="Unsupported file type.",
            )

        stored_filename = self.storage_service.save(
            file=file,
        )

        document = self.document_repository.create(
            user_id=current_user.id,
            original_filename=file.filename,
            stored_filename=stored_filename,
            file_type=extension.removeprefix("."),
        )

        db.add(document)

        try:
            db.commit()
            db.refresh(document)

            self.process_document_service.execute(
                    db=db,
                    document=document,
                )

            db.refresh(document)

        except Exception:
            db.rollback()
            raise

        return document