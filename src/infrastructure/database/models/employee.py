from sqlalchemy import Column, String, DateTime, func, Date
from sqlalchemy.orm import relationship

from ..base import Base


class Employee(Base):
    __tablename__ = "employees"
    id = Column(String(255), primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True, index=True)
    position = Column(String(255), nullable=False)
    department = Column(String(255), nullable=False, index=True)
    start_date = Column(
        Date, nullable=False, default=func.now(), server_default=func.now()
    )
    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=func.now(),
        server_default=func.now(),
    )
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=func.now(),
        server_default=func.now(),
    )

    work_schedules = relationship("WorkSchedule", back_populates="employee")
