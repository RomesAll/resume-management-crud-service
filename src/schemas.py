from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from src.models import Resume, WorkLoad

class BaseDto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class WorkerCreate(BaseDto):
    username: str

class WorkerGet(WorkerCreate):
    id: int
    created_at: datetime
    updated_at: datetime

class WokerUpdate(WorkerCreate):
    id: int = Field(exclude=True)

class ResumeCreate(BaseDto):
    title: str
    workload: WorkLoad
    worker_id: int

class ResumeGet(ResumeCreate):
    id: int
    created_at: datetime
    updated_at: datetime

class ResumeUpdate(ResumeCreate):
    id: int

class VacancyCreate(BaseDto):
    title: str

class VacancyGet(VacancyCreate):
    id: int
    created_at: datetime
    updated_at: datetime

class VacancyUpdate(VacancyCreate):
    id: int

class WorkerRel(WorkerGet):
    resumes: list['ResumeGet']

class ResumeRel():
    worker: 'WorkerGet'
