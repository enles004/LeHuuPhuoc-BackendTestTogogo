from sqlalchemy import Column, String, DateTime, func, ForeignKey, Date
from sqlalchemy.orm import relationship

from ..base import Base


class WorkSchedule(Base):
    __tablename__ = "work_schedules"
    id = Column(String(255), primary_key=True, index=True)
    employee_id = Column(
        String(255), ForeignKey("employees.id", ondelete="CASCADE"), nullable=False
    )
    work_day = Column(Date, nullable=False)
    shift = Column(String(255), nullable=False)
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

    employee = relationship("Employee", back_populates="work_schedules")
