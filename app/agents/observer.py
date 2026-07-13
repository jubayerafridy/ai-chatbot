from app.agents.state import AgentState


class Observer:

    async def observe(
        self,
        state: AgentState,
    ) -> AgentState:

        return state