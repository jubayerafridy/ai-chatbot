from datetime import datetime


class TimeService:

    def execute(
        self,
    ) -> str:

        return datetime.now().isoformat()