from typing import List

from sqlalchemy import select, func

from src.domain.models.employee import Employee as DomainEmployee
from src.domain.ports.employee_repository import EmployeeRepository
from src.infrastructure.database.models.employee import Employee as DBEmployee


class SQLEmployeeRepository(EmployeeRepository):

    def __init__(self, session):
        self._session = session

    async def find_all(
        self, page: int, page_size: int, **kwargs
    ) -> tuple[List[DomainEmployee], int]:
        stmt = select(DBEmployee)

        for field, value in kwargs.items():
            if hasattr(DBEmployee, field):
                stmt = stmt.where(getattr(DBEmployee, field) == value)

        sub_query = stmt.subquery()
        total = await self._session.scalar(select(func.count()).select_from(sub_query))

        offset = (page - 1) * page_size
        stmt = stmt.offset(offset).limit(page_size)

        result = await self._session.execute(stmt)
        employees = result.scalars().all()

        domain_employees = [
            DomainEmployee(
                id=e.id,
                name=e.name,
                email=e.email,
                position=e.position,
                department=e.department,
                start_date=e.start_date,
                created_at=e.created_at,
                updated_at=e.updated_at,
            )
            for e in employees
        ]
        return domain_employees, total

    async def get_employee_by_id(self, id: str) -> DomainEmployee | None:
        result = await self._session.execute(
            select(DBEmployee).where(DBEmployee.id == id)
        )
        orm_obj = result.scalar_one_or_none()

        if not orm_obj:
            return None

        return DomainEmployee(
            id=orm_obj.id,
            name=orm_obj.name,
            email=orm_obj.email,
            position=orm_obj.position,
            department=orm_obj.department,
            start_date=orm_obj.start_date,
            created_at=orm_obj.created_at,
            updated_at=orm_obj.updated_at,
        )

    async def get_employee_by_email(self, email: str) -> DomainEmployee | None:
        result = await self._session.execute(
            select(DBEmployee).where(DBEmployee.email == email)
        )
        orm_obj = result.scalar_one_or_none()

        if not orm_obj:
            return None

        return DomainEmployee(
            id=orm_obj.id,
            name=orm_obj.name,
            email=orm_obj.email,
            position=orm_obj.position,
            department=orm_obj.department,
            start_date=orm_obj.start_date,
            created_at=orm_obj.created_at,
            updated_at=orm_obj.updated_at,
        )

    async def create_employee(self, employee: DomainEmployee) -> DomainEmployee:
        orm_obj = DBEmployee(
            id=employee.id,
            name=employee.name,
            email=employee.email,
            position=employee.position,
            department=employee.department,
            start_date=employee.start_date,
            created_at=employee.created_at,
            updated_at=employee.updated_at,
        )
        self._session.add(orm_obj)
        return employee

    async def update_employee(self, employee: DomainEmployee) -> DomainEmployee:
        pass
