from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.init_db import create_tables
from app.logging.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application starting...")

    create_tables()

    logger.info("Database tables initialized.")

    yield

    logger.info("Application shutting down...")