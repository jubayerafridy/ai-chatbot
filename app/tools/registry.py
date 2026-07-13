from langchain_core.tools import BaseTool

from app.tools.calculator import (
    calculator,
)
from app.tools.time import (
    get_time,
)
from app.tools.retrieval import (
    retrieve_documents,
)


class ToolRegistry:

    def __init__(self):

        self._tools: list[
            BaseTool
        ] = [

            calculator,

            get_time,

            retrieve_documents,

        ]

    def list(
        self,
    ) -> list[BaseTool]:

        return self._tools