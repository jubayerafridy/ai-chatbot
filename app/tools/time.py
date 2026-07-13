from langchain_core.tools import tool

from app.services.tools.time_service import (
    TimeService,
)
from app.services.tools.tool_executor import (
    ToolExecutor,
)


time_service = TimeService()

tool_executor = ToolExecutor()


@tool
async def get_time() -> str:
    """
    Returns the current local time.
    """

    return await tool_executor.execute(
        tool_name="time",
        executor=time_service.execute,
    )