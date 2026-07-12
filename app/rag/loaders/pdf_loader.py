from pathlib import Path

import fitz


class PDFLoader:

    def load(
        self,
        path: Path,
    ) -> str:

        document = fitz.open(path)

        pages: list[str] = []

        for page in document:

            text = page.get_text()

            if text.strip():

                pages.append(text)

        document.close()

        return "\n\n".join(pages)