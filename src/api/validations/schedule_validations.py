from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel


class ScheduleRequest(BaseModel):
    employee_id: str
    work_day: date
    shift: Literal["morning", "afternoon", "full_day"]


class ScheduleResponse(BaseModel):
    id: str
    employee_id: str
    work_day: date
    shift: Literal["morning", "afternoon", "full_day"]
    created_at: datetime
    updated_at: datetime


class ApiResponse(BaseModel):
    message: str
    data: ScheduleResponse
