import datetime
from typing import List

from pydantic import BaseModel, EmailStr


class EmployeeRequest(BaseModel):
    name: str
    email: EmailStr
    position: str
    department: str
    start_date: datetime.date


class EmployeeResponse(BaseModel):
    id: str
    name: str
    email: str
    position: str
    department: str
    start_date: datetime.date
    created_at: datetime.datetime
    updated_at: datetime.datetime


class ApiListResponse(BaseModel):
    message: str
    total: int
    page: int
    page_size: int
    data: List[EmployeeResponse]


class ApiResponse(BaseModel):
    message: str
    data: EmployeeResponse
