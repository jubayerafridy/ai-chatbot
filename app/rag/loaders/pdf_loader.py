from pathlib import Path

from pypdf import PdfReader


class PDFLoader:

    def load(
        self,
        path: Path,
    ) -> str:

        reader = PdfReader(path)

        pages: list[str] = []

        for page in reader.pages:

            text = page.extract_text()

            if text:
                pages.append(text)

        return "\n\n".join(pages)