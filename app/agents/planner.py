from app.agents.state import AgentState


class Planner:

    async def plan(
        self,
        state: AgentState,
    ) -> AgentState:

        if state.get("goal") is None:

            last_message = state["messages"][-1]

            state["goal"] = last_message.content

        if not state.get("plan"):

            state["plan"] = [
                "Understand the request",
                "Decide whether tools are needed",
                "Generate final answer",
            ]

            state["current_step"] = 0

        return state