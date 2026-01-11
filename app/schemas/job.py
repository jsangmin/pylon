from pydantic import BaseModel
from typing import Optional

class JobBase(BaseModel):
    job_name: str
    job_description: Optional[str] = None
    cron_expression: Optional[str] = None
    job_type: str
    enabled_yn: bool = True
    timeout_sec: int = 3600

class JobCreate(JobBase):
    pass

class JobUpdate(BaseModel):
    job_name: Optional[str] = None
    job_description: Optional[str] = None
    cron_expression: Optional[str] = None
    job_type: Optional[str] = None
    enabled_yn: Optional[bool] = None
    timeout_sec: Optional[int] = None

class Job(JobBase):
    job_id: int

    class Config:
        from_attributes = True
