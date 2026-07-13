from app.tools.base.tool import BaseTool
from app.tools.builtin.calculator import (
    CalculatorTool,
)
from app.tools.builtin.time import (
    TimeTool,
)
from app.tools.builtin.retrieval import (
    RetrievalTool,
)

class ToolRegistry:

    def __init__(self):

        self._tools: dict[
            str,
            BaseTool,
        ] = {}

        self.register(
            CalculatorTool(),
        )

        self.register(
            TimeTool(),
        )
        self.register(
    RetrievalTool(),
)

    def register(
        self,
        tool: BaseTool,
    ) -> None:

        self._tools[
            tool.name
        ] = tool

    def get(
        self,
        name: str,
    ) -> BaseTool | None:

        return self._tools.get(
            name,
        )

    def list(self) -> list[BaseTool]:

        return list(
            self._tools.values(),
        )