from app.mcp.service import (
    mcp_service,
)


async def initialize_services() -> None:

    await mcp_service.initialize()