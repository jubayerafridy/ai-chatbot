from datetime import datetime

from app.tools.base.tool import BaseTool


class TimeTool(BaseTool):

    @property
    def name(self) -> str:
        return "time"

    @property
    def description(self) -> str:
        return (
            "Returns the current local date and time."
        )

    async def execute(
        self,
    ) -> str:

        return datetime.now().isoformat()