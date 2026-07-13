class CalculatorService:

    def execute(
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

            return (
                "Invalid mathematical expression."
            )