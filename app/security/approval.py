class HumanApprovalService:

    SENSITIVE_TOOLS = {

        "filesystem",

        "delete_file",

        "execute_sql",

        "run_shell",

    }

    def requires_approval(
        self,
        tool_name: str,
    ) -> bool:

        return tool_name in self.SENSITIVE_TOOLS