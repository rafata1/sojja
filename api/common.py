from typing import Any


class DataResponse:
    code: int
    message: str
    data: Any

    def success(self, data: Any = None, message: str = "Success"):
        self.code = 200
        self.message = message
        self.data = data
        return self
