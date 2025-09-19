class ServerError(Exception):
    def __init__(
        self,
        message: str = "Server error",
        error_code: str = "SERVER_ERROR",
        status_code: int = 500,
    ):
        self.message = message
        self.error_code = error_code
        self.status_code = status_code
