from langchain_core.tools import BaseTool

from app.mcp.service import (
    mcp_service,
)
from app.tools.calculator import (
    calculator,
)
from app.tools.retrieval import (
    retrieve_documents,
)
from app.tools.time import (
    get_time,
)


class ToolRegistry:

    def __init__(self):

        self._tools: list[
            BaseTool
        ] = [

            calculator,

            get_time,

            retrieve_documents,

        ]

        self._tools.extend(
            mcp_service.get_tools(),
        )

    def register(
        self,
        tool: BaseTool,
    ) -> None:

        self._tools.append(
            tool,
        )

    def list(
        self,
    ) -> list[BaseTool]:

        return self._tools