from src.app.dto.employees.list_employee import ListEmployeeCommand
from src.domain.services.unit_of_work import UnitOfWork
from src.app.dto.employees.list_employee import ListEmployeeResponse
import attrs as at


class ListEmployeeUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(self, command: ListEmployeeCommand):
        async with self._uow:
            attrs = command.__dict__
            filters = {
                k: v
                for k, v in attrs.items()
                if k not in ["page", "page_size"] and v is not None
            }
            employees, total = await self._uow.employee_repository.find_all(
                page=command.page, page_size=command.page_size, **filters
            )

            return ListEmployeeResponse(
                employees=employees,
                page=command.page,
                page_size=command.page_size,
                total=total,
            )
