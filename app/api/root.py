from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():
    return {
        "message": "AI AppSec Assistant API is running!"
    }