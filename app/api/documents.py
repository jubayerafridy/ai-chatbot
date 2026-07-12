from fastapi import (
    APIRouter,
    Depends,
    File,
    UploadFile,
)
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.document import DocumentResponse
from app.services.rag.upload_document_service import (
    UploadDocumentService,
)

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)

upload_document_service = UploadDocumentService()


@router.post(
    "/upload",
    response_model=DocumentResponse,
    status_code=201,
)
def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return upload_document_service.execute(
        db=db,
        current_user=current_user,
        file=file,
    )