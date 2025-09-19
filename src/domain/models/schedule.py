import uuid
from datetime import datetime, timezone, date
from typing import Literal

import attrs

from src.domain.models.employee import Employee


@attrs.define(slots=False, kw_only=True)
class WorkSchedule:
    id: str
    employee_id: str
    work_day: date
    shift: str
    created_at: datetime
    updated_at: datetime

    _employee: "Employee" = attrs.field(init=False)

    @property
    def employee(self) -> "Employee":
        return self._employee

    @employee.setter
    def employee(self, employee: "Employee") -> None:
        self._employee = employee

    @staticmethod
    async def _generate_id(self) -> str:
        return str(uuid.uuid4().hex)

    @classmethod
    async def create(
        cls, employee_id: str, work_day: date, shift: str
    ) -> "WorkSchedule":
        id = await cls._generate_id(cls)
        now = datetime.now(timezone.utc)
        return cls(
            id=id,
            employee_id=employee_id,
            work_day=work_day,
            shift=shift,
            created_at=now,
            updated_at=now,
        )
