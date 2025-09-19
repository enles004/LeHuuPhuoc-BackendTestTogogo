import config
from src.infrastructure.database.sessions import create_session
from src.app.use_cases import employees
from src.app.use_cases import schedules
from src.domain.services.bus import BusCommand
from src.infrastructure.services.sql_unit_of_work import SQLAlchemyUnitOfWork

# session
session_factory = create_session()

# services
unit_of_work = SQLAlchemyUnitOfWork(session_factory)
command_bus = BusCommand()

command_bus.register(
    employees.CreateEmployeeCommand, employees.CreateEmployeeUseCase(unit_of_work)
)
command_bus.register(
    employees.ListEmployeeCommand, employees.ListEmployeeUseCase(unit_of_work)
)

command_bus.register(
    schedules.UpdateScheduleCommand, schedules.UpdateScheduleUseCase(unit_of_work)
)


async def get_command_bus():
    return command_bus
