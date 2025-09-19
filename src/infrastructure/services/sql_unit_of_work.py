from sqlalchemy.ext.asyncio.session import AsyncSession, async_sessionmaker

from ..repositories.employee_repository import SQLEmployeeRepository
from ..repositories.schedule_repository import SQLWorkScheduleRepository
from ...domain.services.unit_of_work import UnitOfWork


class SQLAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]):
        self.session_factory = session_factory
        self.session: AsyncSession | None = None

    async def __aenter__(self):
        self.session = self.session_factory()
        self.employee_repository = SQLEmployeeRepository(self.session)
        self.work_schedule_repository = SQLWorkScheduleRepository(self.session)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if exc_type:
            await self.rollback()
        else:
            await self.commit()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
