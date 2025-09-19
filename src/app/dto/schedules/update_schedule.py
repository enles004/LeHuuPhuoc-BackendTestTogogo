import datetime
from dataclasses import dataclass


@dataclass
class UpdateScheduleCommand:
    employee_id: str
    work_day: datetime.date
    shift: str


@dataclass
class UpdateScheduleResponse:
    id: str
    employee_id: str
    work_day: datetime.date
    shift: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
