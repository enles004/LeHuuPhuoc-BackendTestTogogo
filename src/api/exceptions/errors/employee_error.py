class EmployeeError(Exception):
    def __init__(
        self,
        message: str = "Employee error",
        error_code: str = "EMPLOYEE_ERROR",
        status_code: int = 400,
    ):
        self.message = message
        self.error_code = error_code
        self.status_code = status_code


class EmployeeAlreadyExists(EmployeeError):
    def __init__(self):
        super().__init__(
            message="Email already exists",
            error_code="EMPLOYEE_ALREADY_EXISTS",
            status_code=409,
        )


class EmployeeNotFound(EmployeeError):
    def __init__(self):
        super().__init__(
            message="Employee not found",
            error_code="EMPLOYEE_NOT_FOUND",
            status_code=404,
        )
