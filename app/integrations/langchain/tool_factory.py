from langchain_core.tools import StructuredTool

from app.tools.base.tool import BaseTool


class ToolFactory:

    @staticmethod
    def create(
        tool: BaseTool,
    ) -> StructuredTool:

        async def wrapper(
            **kwargs,
        ):

            return await tool.execute(
                **kwargs,
            )

        return StructuredTool.from_function(
            coroutine=wrapper,
            name=tool.name,
            description=tool.description,
        )