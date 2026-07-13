from langchain_core.messages import HumanMessage

from app.agents.agent import Agent
from app.guardrails.service import (
    GuardrailService,
)


class AgentService:

    def __init__(self):

        self.agent = Agent()

        self.guardrails = (
            GuardrailService()
        )

    async def execute(
        self,
        message: str,
        thread_id: str,
    ) -> str:

        result = await self.agent.run(
            messages=[
                HumanMessage(
                    content=message,
                )
            ],
            thread_id=thread_id,
        )

        assistant_text = (
            self.guardrails.validate_output(
                result["messages"][-1].content,
            )
        )

        return assistant_text