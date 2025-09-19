from fastapi import FastAPI
from starlette.responses import RedirectResponse

from .exceptions import errors
from .exceptions.handlers import (
    validation_exception_handler,
    employee_error_handler,
    server_error_handler,
)
from .routes import employee
from .routes import schedule


def create_app():
    app = FastAPI(title="Employee API", version="0.1.0")

    # register handlers
    app.add_exception_handler(Exception, server_error_handler)
    app.add_exception_handler(errors.EmployeeError, employee_error_handler)
    app.add_exception_handler(errors.ValidationError, validation_exception_handler)

    # register routes
    app.include_router(employee.router, prefix="/api/v1", tags=["employee"])
    app.include_router(schedule.router, prefix="/api/v1", tags=["schedule"])

    @app.get("/", include_in_schema=False)
    async def root():
        return RedirectResponse(url="/docs")

    return app
