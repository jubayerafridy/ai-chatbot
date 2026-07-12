from langchain_ollama import ChatOllama
from langchain_core.tools import tool


@tool
def get_time() -> str:
    """Returns the current time."""
    return "10:30 AM"


llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0,
)

llm_with_tools = llm.bind_tools(
    [get_time],
)

response = llm_with_tools.invoke(
    "What time is it?"
)

print(response)
print(response.tool_calls)