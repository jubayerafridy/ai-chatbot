class ToolPolicy:

    ALLOWED_TOOLS = {

        "calculator",

        "time",

        "retrieve_documents",

    }

    @classmethod
    def is_allowed(
        cls,
        tool_name: str,
    ) -> bool:

        return tool_name in cls.ALLOWED_TOOLS