from abc import ABC, abstractmethod
from src.domain.ports.employee_repository import EmployeeRepository
from src.domain.ports.schedule_repository import WorkScheduleRepository


class UnitOfWork(ABC):
    employee_repository: EmployeeRepository
    work_schedule_repository: WorkScheduleRepository

    @abstractmethod
    async def __aenter__(self):
        pass

    @abstractmethod
    async def __aexit__(self, exc_type, exc, tb):
        pass

    @abstractmethod
    async def commit(self):
        pass

    @abstractmethod
    async def rollback(self):
        pass
