from pathlib import Path

from app.rag.loaders.pdf_loader import PDFLoader
from app.rag.splitters.text_splitter import TextSplitter

loader = PDFLoader()

text = loader.load(
    Path(
        "storage/documents/72206cc0-838c-456a-98ec-0e555049969a.pdf"
    )
)

splitter = TextSplitter()

chunks = splitter.split(text)

print(f"Chunks: {len(chunks)}")

print()

print(chunks[0])