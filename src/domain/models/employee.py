import uuid
from datetime import datetime, timezone, date
import attrs

from src.infrastructure.database.models.work_schedule import WorkSchedule


@attrs.define(slots=False, kw_only=True)
class Employee:
    id: str
    name: str
    email: str
    position: str
    department: str
    start_date: date
    created_at: datetime
    updated_at: datetime

    _work_schedules: "WorkSchedule" = attrs.field(init=False)

    @property
    def work_schedules(self) -> "WorkSchedule":
        return self._work_schedules

    @work_schedules.setter
    def work_schedules(self, work_schedules: "WorkSchedule") -> None:
        self._work_schedules = work_schedules

    @staticmethod
    async def _generate_id(self) -> str:
        return str(uuid.uuid4().hex)

    @classmethod
    async def create(
        cls,
        name: str,
        email: str,
        position: str,
        department: str,
        start_date: date,
    ) -> "Employee":
        employee_id = await cls._generate_id(cls)
        now = datetime.now(timezone.utc)
        return cls(
            id=employee_id,
            name=name,
            email=email,
            position=position,
            department=department,
            start_date=start_date,
            created_at=now,
            updated_at=now,
        )
