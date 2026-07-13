from typing import TypedDict

from langchain_core.messages import BaseMessage


class AgentState(TypedDict):

    messages: list[BaseMessage]

    goal: str | None

    plan: list[str]

    current_step: int


#     messages

# goal

# plan

# current_step

# completed_steps

# tool_results

# memory