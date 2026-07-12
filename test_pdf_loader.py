from pathlib import Path

from app.rag.loaders.pdf_loader import PDFLoader

loader = PDFLoader()

text = loader.load(
    Path("storage/documents/72206cc0-838c-456a-98ec-0e555049969a.pdf")
)

print(text[:1000])