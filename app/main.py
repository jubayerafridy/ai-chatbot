from fastapi import FastAPI

from app.api.root import router as root_router
from app.api.health import router as health_router
from app.logging.logger import logger
from app.core.settings import settings
from app.core.lifespan import lifespan
from app.api.auth import router as auth_router
from app.api.users import router as users_router
from app.api.chats import router as chats_router
from app.api.llm import router as llm_router


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)

logger.info("Starting AI AppSec Assistant")

app.include_router(root_router)
app.include_router(health_router)
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(chats_router)
app.include_router(llm_router)


# uvicorn app.main:app --reload