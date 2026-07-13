from langchain_core.tools import tool

from app.services.tools.calculator_service import (
    CalculatorService,
)


calculator_service = (
    CalculatorService()
)


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

    return calculator_service.execute(
        expression,
    )