from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NoticeBase(BaseModel):
    title: str
    content: str
    is_pinned: Optional[bool] = False

class NoticeCreate(NoticeBase):
    writer_id: int

class NoticeUpdate(NoticeBase):
    title: Optional[str] = None
    content: Optional[str] = None
    is_pinned: Optional[bool] = None

class Notice(NoticeBase):
    id: int
    writer_id: int
    view_count: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
