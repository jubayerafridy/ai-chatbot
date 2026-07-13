from app.agents.state import AgentState


class Executor:

    async def execute(
        self,
        state: AgentState,
    ) -> AgentState:

        if state["current_step"] < len(
            state["plan"]
        ):

            state["current_step"] += 1

        return state