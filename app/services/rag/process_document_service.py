from pathlib import Path

from sqlalchemy.orm import Session

from app.models.document import (
    Document,
    DocumentStatus,
)
from app.models.document_chunk import (
    DocumentChunk,
)
from app.rag.loaders.pdf_loader import PDFLoader
from app.rag.splitters.text_splitter import (
    TextSplitter,
)
from app.repositories.document_chunk_repository import (
    DocumentChunkRepository,
)
from app.services.rag.vector_index_service import (
    VectorIndexService,
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

        self.vector_index_service = (
            VectorIndexService()
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

        document_path = (
            self.STORAGE_DIRECTORY
            / document.stored_filename
        )

        text = self.loader.load(
            document_path,
        )

        chunks = self.splitter.split(
            text,
        )

        saved_chunks: list[
            DocumentChunk
        ] = []

        for index, chunk in enumerate(
            chunks,
        ):

            entity = (
                self.chunk_repository.create(
                    document_id=document.id,
                    chunk_index=index,
                    content=chunk,
                )
            )

            db.add(
                entity,
            )

            saved_chunks.append(
                entity,
            )

        db.commit()

        for chunk in saved_chunks:

            db.refresh(
                chunk,
            )

        self.vector_index_service.index_chunks(
            saved_chunks,
        )

        document.status = (
            DocumentStatus.READY
        )

        db.commit()