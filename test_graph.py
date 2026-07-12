import asyncio

from app.services.ai.langgraph_service import (
    LangGraphService,
)


async def main():

    service = LangGraphService()

    response = await service.execute(
        "What time is it?"
    )

    print(response)


asyncio.run(main())