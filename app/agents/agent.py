from app.langgraph.app import graph


class Agent:

    async def run(
        self,
        messages,
        thread_id: str,
    ):

        return await graph.ainvoke(
            {
                "messages": messages,
            },
            config={
                "configurable": {
                    "thread_id": thread_id,
                }
            },
        )