from pathlib import Path

from sqlalchemy.orm import Session

from app.models.document import (
    Document,
    DocumentStatus,
)
from app.rag.loaders.pdf_loader import PDFLoader
from app.rag.splitters.text_splitter import (
    TextSplitter,
)
from app.repositories.document_chunk_repository import (
    DocumentChunkRepository,
)


class ProcessDocumentService:

    STORAGE_DIRECTORY = Path(
        "storage/documents"
    )

    def __init__(self):

        self.loader = PDFLoader()

        self.splitter = TextSplitter()

        self.chunk_repository = (
            DocumentChunkRepository()
        )

    def execute(
        self,
        db: Session,
        document: Document,
    ) -> None:

        document.status = (
            DocumentStatus.PROCESSING
        )

        db.commit()

        pdf_path = (
            self.STORAGE_DIRECTORY
            / document.stored_filename
        )

        text = self.loader.load(
            pdf_path,
        )

        chunks = self.splitter.split(
            text,
        )

        for index, chunk in enumerate(chunks):

            entity = (
                self.chunk_repository.create(
                    document_id=document.id,
                    chunk_index=index,
                    content=chunk,
                )
            )

            db.add(entity)

        document.status = (
            DocumentStatus.READY
        )

        db.commit()