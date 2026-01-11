from sqlalchemy import Column, Integer, String, Boolean, Text
from app.core.database import Base

class Job(Base):
    __tablename__ = "tb_job"

    job_id = Column(Integer, primary_key=True, index=True)
    job_name = Column(String, unique=True, index=True, nullable=False)
    job_description = Column(Text, nullable=True)
    cron_expression = Column(String, nullable=True)
    job_type = Column(String, nullable=False)  # BATCH / SCHEDULE / MANUAL
    enabled_yn = Column(Boolean, default=True)
    timeout_sec = Column(Integer, default=3600)
