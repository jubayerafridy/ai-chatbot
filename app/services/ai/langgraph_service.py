from langchain_core.messages import (
    HumanMessage,
)

from app.langgraph.app import graph


class LangGraphService:

    async def execute(
        self,
        message: str,
        thread_id: str,
    ) -> str:

        result = await graph.ainvoke(
            {
                "messages": [
                    HumanMessage(
                        content=message,
                    )
                ]
            },
            config={
                "configurable": {
                    "thread_id": thread_id,
                }
            },
        )

        return result["messages"][-1].content