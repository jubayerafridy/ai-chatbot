from langgraph.prebuilt import ToolNode

from app.tools.registry import (
    ToolRegistry,
)


registry = ToolRegistry()

tool_node = ToolNode(
    tools=registry.list(),
)