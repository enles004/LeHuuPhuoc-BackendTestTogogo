from dataclasses import dataclass
import datetime
from typing import List, Dict
from src.domain.models.employee import Employee


@dataclass
class ListEmployeeCommand:
    department: str
    start_date_after: datetime.date
    page: int
    page_size: int


@dataclass
class ListEmployeeResponse:
    employees: List[Employee]
    page: int
    page_size: int
    total: int
