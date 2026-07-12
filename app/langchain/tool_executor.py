from typing import Any

from app.tools.registry import ToolRegistry


class ToolExecutor:

    def __init__(self):

        self.registry = ToolRegistry()

    async def execute(
        self,
        tool_name: str,
        arguments: dict[str, Any],
    ) -> Any:

        tool = self.registry.get(
            tool_name,
        )

        if tool is None:

            raise ValueError(
                f"Unknown tool: {tool_name}"
            )

        return await tool.execute(
            **arguments,
        )