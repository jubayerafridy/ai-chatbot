class MCPClient:

    def __init__(self):

        self.servers = []

    def register(
        self,
        server,
    ):

        self.servers.append(
            server,
        )

    def list_servers(
        self,
    ):

        return self.servers