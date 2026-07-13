from langchain_core.tools import BaseTool

from app.mcp.client import (
    client,
)


class MCPService:

    def __init__(self):

        self._initialized = False

        self._tools: list[
            BaseTool
        ] = []

    async def initialize(
        self,
    ) -> None:

        if self._initialized:
            return

        self._tools = await client.get_tools()

        self._initialized = True

    def get_tools(
        self,
    ) -> list[BaseTool]:

        return self._tools


mcp_service = MCPService()