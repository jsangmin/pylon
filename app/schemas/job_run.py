from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class JobRunBase(BaseModel):
    job_id: int
    run_status: str
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    exit_code: Optional[int] = None
    error_message: Optional[str] = None

class JobRunCreate(JobRunBase):
    pass

class JobRunUpdate(BaseModel):
    run_status: Optional[str] = None
    end_time: Optional[datetime] = None
    exit_code: Optional[int] = None
    error_message: Optional[str] = None

class JobRun(JobRunBase):
    job_run_id: int

    class Config:
        from_attributes = True
