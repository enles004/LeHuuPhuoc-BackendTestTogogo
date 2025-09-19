from src.api.exceptions.errors.employee_error import EmployeeAlreadyExists
from src.app.dto.employees.create_employee import (
    CreateEmployeeCommand,
    CreateEmployeeResponse,
)
from src.domain.models.employee import Employee
from src.domain.services.unit_of_work import UnitOfWork


class CreateEmployeeUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(self, command: CreateEmployeeCommand) -> CreateEmployeeResponse:
        async with self._uow:
            find_employee = await self._uow.employee_repository.get_employee_by_email(
                email=command.email
            )
            if find_employee:
                raise EmployeeAlreadyExists()

            new_employee = await Employee.create(
                name=command.name,
                email=command.email,
                position=command.position,
                department=command.department,
                start_date=command.start_date,
            )

            await self._uow.employee_repository.create_employee(employee=new_employee)

            return CreateEmployeeResponse(
                id=new_employee.id,
                name=new_employee.name,
                email=new_employee.email,
                position=new_employee.position,
                department=new_employee.department,
                start_date=new_employee.start_date,
                created_at=new_employee.created_at,
                updated_at=new_employee.updated_at,
            )
