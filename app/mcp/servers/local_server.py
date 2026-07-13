from datetime import datetime
import platform

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("AI Chatbot")


@mcp.tool()
def get_time() -> str:
    return datetime.now().isoformat()


@mcp.tool()
def get_os() -> str:
    """
    Return operating system.
    """
    return platform.platform()


if __name__ == "__main__":
    mcp.run()