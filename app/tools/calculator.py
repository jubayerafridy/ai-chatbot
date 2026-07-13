from langchain_core.tools import tool

from app.services.tools.calculator_service import (
    CalculatorService,
)
from app.services.tools.tool_executor import (
    ToolExecutor,
)


calculator_service = CalculatorService()

tool_executor = ToolExecutor()


@tool
async def calculator(
    expression: str,
) -> str:
    """
    Evaluate a mathematical expression.

    Example:
    2 + 2
    (10 * 5) + 8
    """

    return await tool_executor.execute(
        tool_name="calculator",
        executor=calculator_service.execute,
        expression=expression,
    )