from app.schemas.tool_call import ToolCall
from app.tools.registry import ToolRegistry
from app.security.tool_permissions import (
    ToolPermissionService,
)


class ToolRunner:

    def __init__(self):

        self.registry = ToolRegistry()

        self.permissions = (
            ToolPermissionService()
        )

    async def run(
        self,
        tool_call: ToolCall,
    ) -> str:

        tool = self.registry.get(
            tool_call.name,
        )

        if tool is None:

            raise ValueError(
                f"Unknown tool: {tool_call.name}"
            )

        # Permission check
        self.permissions.validate(
            tool_call.name,
        )

        result = await tool.execute(
            **tool_call.arguments,
        )

        return str(result)