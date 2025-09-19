from datetime import date

from sqlalchemy import select, update, and_

from src.domain.models.schedule import WorkSchedule as DomainWorkSchedule
from src.domain.ports.schedule_repository import WorkScheduleRepository
from src.infrastructure.database.models.work_schedule import (
    WorkSchedule as DBWorkSchedule,
)


class SQLWorkScheduleRepository(WorkScheduleRepository):
    def __init__(self, session):
        self._session = session

    async def get_schedule_by_employee_id_and_work_day(
        self, employee_id: str, work_day: date
    ) -> DomainWorkSchedule:
        stmt = select(DBWorkSchedule).where(
            and_(
                DBWorkSchedule.employee_id == employee_id,
                DBWorkSchedule.work_day == work_day,
            )
        )

        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def create_schedule(self, schedule: DomainWorkSchedule) -> DomainWorkSchedule:
        orm_obj = DBWorkSchedule(
            id=schedule.id,
            employee_id=schedule.employee_id,
            work_day=schedule.work_day,
            shift=schedule.shift,
            created_at=schedule.created_at,
            updated_at=schedule.updated_at,
        )
        self._session.add(orm_obj)
        return schedule

    async def update_shift_schedule_by_employee_id_and_work_day(
        self, schedule: DomainWorkSchedule
    ) -> DomainWorkSchedule:
        stmt = (
            update(DBWorkSchedule)
            .where(
                and_(
                    DBWorkSchedule.employee_id == schedule.employee_id,
                    DBWorkSchedule.work_day == schedule.work_day,
                )
            )
            .values(shift=schedule.shift, updated_at=schedule.updated_at)
            .returning(DBWorkSchedule)
        )

        result = await self._session.execute(stmt)

        db_schedule = result.scalar_one()

        return DomainWorkSchedule(
            id=db_schedule.id,
            employee_id=db_schedule.employee_id,
            work_day=db_schedule.work_day,
            shift=db_schedule.shift,
            created_at=db_schedule.created_at,
            updated_at=db_schedule.updated_at,
        )
