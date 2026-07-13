import inspect
from typing import Any, Callable

from app.security.approval import (
    HumanApprovalService,
)
from app.security.tool_permissions import (
    ToolPermissionService,
)


class ToolExecutor:

    def __init__(self):

        self.permission_service = (
            ToolPermissionService()
        )

        self.approval_service = (
            HumanApprovalService()
        )

    async def execute(
        self,
        tool_name: str,
        executor: Callable[..., Any],
        **kwargs,
    ) -> Any:

        self.permission_service.validate(
            tool_name,
        )

        if self.approval_service.requires_approval(
            tool_name,
        ):

            raise PermissionError(
                f"Tool '{tool_name}' requires human approval."
            )

        result = executor(
            **kwargs,
        )

        if inspect.isawaitable(
            result,
        ):

            return await result

        return result