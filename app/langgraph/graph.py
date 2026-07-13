from langgraph.graph import (
    START,
    StateGraph,
)
from langgraph.prebuilt import (
    tools_condition,
)

from app.langgraph.state import ChatState
from app.langgraph.nodes.chat_node import (
    ChatNode,
)
from app.langgraph.nodes.tool_node import (
    tool_node,
)

builder = StateGraph(ChatState)

builder.add_node(
    "chatbot",
    ChatNode(),
)

builder.add_node(
    "tools",
    tool_node,
)

builder.add_edge(
    START,
    "chatbot",
)

builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)

builder.add_edge(
    "tools",
    "chatbot",
)