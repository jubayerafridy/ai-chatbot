from langchain_mcp_adapters.client import (
    MultiServerMCPClient,
)


client = MultiServerMCPClient(
    {
        "local": {
            "command": "python",
            "args": [
                "app/mcp/servers/local_server.py",
            ],
            "transport": "stdio",
        }
    }
)