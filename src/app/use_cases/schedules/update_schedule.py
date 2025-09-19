from src.api.exceptions.errors.employee_error import EmployeeNotFound
from src.app.dto.schedules.update_schedule import (
    UpdateScheduleCommand,
    UpdateScheduleResponse,
)
from src.domain.models.schedule import WorkSchedule
from src.domain.services.unit_of_work import UnitOfWork


class UpdateScheduleUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(self, command: UpdateScheduleCommand):
        async with self._uow:
            if not await self._uow.employee_repository.get_employee_by_id(
                id=command.employee_id
            ):
                raise EmployeeNotFound()

            new_schedule = await WorkSchedule.create(
                employee_id=command.employee_id,
                work_day=command.work_day,
                shift=command.shift,
            )

            schedule_exits = await self._uow.work_schedule_repository.get_schedule_by_employee_id_and_work_day(
                employee_id=command.employee_id, work_day=command.work_day
            )

            if schedule_exits:
                updated_schedule = await self._uow.work_schedule_repository.update_shift_schedule_by_employee_id_and_work_day(
                    schedule=new_schedule
                )

                return (
                    UpdateScheduleResponse(
                        id=updated_schedule.id,
                        employee_id=updated_schedule.employee_id,
                        work_day=updated_schedule.work_day,
                        shift=updated_schedule.shift,
                        created_at=updated_schedule.created_at,
                        updated_at=updated_schedule.updated_at,
                    ),
                    "Schedule updated",
                )

            await self._uow.work_schedule_repository.create_schedule(
                schedule=new_schedule
            )

            return (
                UpdateScheduleResponse(
                    id=new_schedule.id,
                    employee_id=new_schedule.employee_id,
                    work_day=new_schedule.work_day,
                    shift=new_schedule.shift,
                    created_at=new_schedule.created_at,
                    updated_at=new_schedule.updated_at,
                ),
                "Schedule created",
            )
