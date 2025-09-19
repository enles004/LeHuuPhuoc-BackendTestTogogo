from abc import ABC, abstractmethod
from typing import List

from src.domain.models.employee import Employee


class EmployeeRepository(ABC):

    @abstractmethod
    async def get_employee_by_id(self, id: str) -> Employee:
        raise NotImplementedError

    @abstractmethod
    async def get_employee_by_email(self, email: str) -> Employee:
        raise NotImplementedError

    @abstractmethod
    async def create_employee(self, employee: Employee) -> Employee:
        raise NotImplementedError

    @abstractmethod
    async def update_employee(self, employee: Employee) -> Employee:
        raise NotImplementedError

    @abstractmethod
    async def find_all(
        self, page: int, page_size: int, **kwargs
    ) -> tuple[List[Employee], int]:
        raise NotImplementedError
