import datetime
from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class CreateEmployeeCommand:
    name: str
    email: str
    position: str
    department: str
    start_date: datetime.date


@dataclass
class CreateEmployeeResponse:
    id: str
    name: str
    email: str
    position: str
    department: str
    start_date: datetime.date
    created_at: datetime.datetime
    updated_at: datetime.datetime
