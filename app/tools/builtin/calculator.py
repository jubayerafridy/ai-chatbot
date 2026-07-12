from app.tools.base.tool import BaseTool


class CalculatorTool(BaseTool):

    @property
    def name(self) -> str:
        return "calculator"

    @property
    def description(self) -> str:
        return (
            "Performs basic mathematical calculations."
        )

    async def execute(
        self,
        expression: str,
    ) -> str:

        try:

            result = eval(
                expression,
                {
                    "__builtins__": {},
                },
                {},
            )

            return str(result)

        except Exception:

            return "Invalid mathematical expression."