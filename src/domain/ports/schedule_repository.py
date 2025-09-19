from abc import ABC, abstractmethod
from datetime import date
from src.domain.models.schedule import WorkSchedule


class WorkScheduleRepository(ABC):

    @abstractmethod
    async def get_schedule_by_employee_id_and_work_day(
        self, employee_id: str, work_day: date
    ) -> WorkSchedule:
        raise NotImplementedError

    @abstractmethod
    async def update_shift_schedule_by_employee_id_and_work_day(
        self, schedule: WorkSchedule
    ) -> WorkSchedule:
        raise NotImplementedError

    @abstractmethod
    async def create_schedule(self, schedule: WorkSchedule) -> WorkSchedule:
        raise NotImplementedError
