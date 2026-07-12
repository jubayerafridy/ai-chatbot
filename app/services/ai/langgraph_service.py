from langchain_core.messages import (
    HumanMessage,
)

from app.langgraph.app import graph


class LangGraphService:

    async def execute(
        self,
        message: str,
    ) -> str:

        result = await graph.ainvoke(
            {
                "messages": [
                    HumanMessage(
                        content=message,
                    )
                ]
            }
        )

        return result["messages"][-1].content