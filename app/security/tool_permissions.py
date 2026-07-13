from app.security.policy import (
    ToolPolicy,
)


class ToolPermissionService:

    def validate(
        self,
        tool_name: str,
    ) -> None:

        if not ToolPolicy.is_allowed(
            tool_name,
        ):

            raise PermissionError(
                f"Tool '{tool_name}' is not allowed."
            )