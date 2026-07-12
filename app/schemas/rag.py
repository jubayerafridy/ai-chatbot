from pydantic import BaseModel


class RetrievedChunk(BaseModel):

    document_id: int

    chunk_index: int

    content: str

    score: float