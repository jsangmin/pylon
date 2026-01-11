from pydantic import BaseModel
from typing import Optional

class JobHistoryBase(BaseModel):
    job_id: int
    job_name: str
    cron_expression: Optional[str] = None
    enabled_yn: bool = True
    changed_reason: Optional[str] = None

class JobHistoryCreate(JobHistoryBase):
    pass

class JobHistoryUpdate(BaseModel):
    job_name: Optional[str] = None
    cron_expression: Optional[str] = None
    enabled_yn: Optional[bool] = None
    changed_reason: Optional[str] = None

class JobHistory(JobHistoryBase):
    job_history_id: int

    class Config:
        from_attributes = True
