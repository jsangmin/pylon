from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class JobRunHistoryBase(BaseModel):
    job_run_id: int
    job_id: int
    run_status: str
    start_time: datetime
    end_time: Optional[datetime] = None
    duration_ms: Optional[int] = None
    exit_code: Optional[int] = None
    error_stacktrace: Optional[str] = None

class JobRunHistoryCreate(JobRunHistoryBase):
    pass

class JobRunHistoryUpdate(BaseModel):
    run_status: Optional[str] = None
    end_time: Optional[datetime] = None
    duration_ms: Optional[int] = None
    exit_code: Optional[int] = None
    error_stacktrace: Optional[str] = None

class JobRunHistory(JobRunHistoryBase):
    job_run_history_id: int

    class Config:
        from_attributes = True
