from fastapi import APIRouter, Body
from fastapi.params import Depends

from ..validations.schedule_validations import (
    ScheduleRequest,
    ApiResponse,
    ScheduleResponse,
)
from ...app.dto.schedules.update_schedule import UpdateScheduleCommand
from ...dependencies import get_command_bus
from src.domain.services.bus import BusCommand

router = APIRouter()

# @router.put("/schedule")
# async def update_schedule():
#     return {"message": "Schedule updated"}
#
# @router.post("/schedule")
# async def create_schedule():
#     return {"message": "Schedule created"}


@router.put("/work-schedules", status_code=200, response_model=ApiResponse)
async def update_auto_schedule(
    body: ScheduleRequest = Body(embed=False),
    bus: BusCommand = Depends(get_command_bus),
):
    command = UpdateScheduleCommand(
        employee_id=body.employee_id, work_day=body.work_day, shift=body.shift
    )

    schedule, message = await bus.execute(command)

    return ApiResponse(message=message, data=ScheduleResponse(**schedule.__dict__))
