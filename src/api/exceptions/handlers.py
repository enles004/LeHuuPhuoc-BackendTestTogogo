from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from .errors.employee_error import EmployeeError


async def employee_error_handler(request: Request, exc: EmployeeError):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.message,
            "error_code": exc.error_code,
            "status_code": exc.status_code,
        },
    )


async def server_error_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "error_code": "server_error",
            "status_code": 500,
        },
    )


async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "error": "Validation failed",
            "error_code": "validation_error",
            "status_code": 422,
            "detail": exc.errors(),
        },
    )
