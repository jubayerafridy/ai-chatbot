from langchain_core.tools import tool

from app.services.tools.time_service import (
    TimeService,
)


time_service = (
    TimeService()
)


@tool
async def get_time() -> str:
    """
    Return the current local date and time.
    """

    return time_service.execute()