import datetime

from fastapi import APIRouter, Body, Depends, Query

from src.app.dto.employees.create_employee import CreateEmployeeCommand
from src.dependencies import get_command_bus
from src.domain.services.bus import BusCommand
from ..validations.employee_validations import (
    ApiResponse,
    EmployeeRequest,
    EmployeeResponse,
    ApiListResponse,
)
from ...app.dto.employees.list_employee import ListEmployeeCommand

router = APIRouter()


@router.post("/employees", status_code=201, response_model=ApiResponse)
async def create_employee(
    body: EmployeeRequest = Body(embed=False),
    bus: BusCommand = Depends(get_command_bus),
):
    command = CreateEmployeeCommand(
        name=body.name,
        email=str(body.email),
        position=body.position,
        department=body.department,
        start_date=body.start_date,
    )

    employee = await bus.execute(command)

    return ApiResponse(
        message="Employee created successfully",
        data=EmployeeResponse(**employee.__dict__),
    )


@router.get("/employees", response_model=ApiListResponse, status_code=200)
async def list_employees(
    department: str = Query(None, description="Filter by department"),
    start_date_after: datetime.date = Query(
        None, description="Filter employees who started after this date YYYY-MM-DD"
    ),
    page: int = Query(1, ge=1, description="Page number (starting from 1)"),
    page_size: int = Query(10, ge=1, le=100, description="Items per page"),
    bus: BusCommand = Depends(get_command_bus),
):
    command = ListEmployeeCommand(
        department=department,
        start_date_after=start_date_after,
        page=page,
        page_size=page_size,
    )

    result = await bus.execute(command=command)

    return ApiListResponse(
        message="Employees fetched successfully",
        total=result.total,
        page=result.page,
        page_size=result.page_size,
        data=[EmployeeResponse(**employee.__dict__) for employee in result.employees],
    )
