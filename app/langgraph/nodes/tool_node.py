from langgraph.prebuilt import ToolNode

from app.integrations.langchain.tool_factory import (
    ToolFactory,
)
from app.tools.registry import ToolRegistry


registry = ToolRegistry()

tools = [
    ToolFactory.create(tool)
    for tool in registry.list()
]

tool_node = ToolNode(
    tools=tools,
)