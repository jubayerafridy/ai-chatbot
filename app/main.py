from fastapi import FastAPI

from app.api.root import router as root_router
from app.api.health import router as health_router

app = FastAPI()

app.include_router(root_router)
app.include_router(health_router)

# uvicorn app.main:app --reload