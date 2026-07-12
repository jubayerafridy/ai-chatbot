from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile


class LocalStorageService:

    STORAGE_DIRECTORY = Path(
        "storage/documents"
    )

    def save(
        self,
        file: UploadFile,
    ) -> str:

        self.STORAGE_DIRECTORY.mkdir(
            parents=True,
            exist_ok=True,
        )

        extension = (
            Path(file.filename)
            .suffix
            .lower()
        )

        stored_filename = (
            f"{uuid4()}{extension}"
        )

        destination = (
            self.STORAGE_DIRECTORY
            / stored_filename
        )

        with destination.open("wb") as buffer:

            buffer.write(
                file.file.read()
            )

        return stored_filename