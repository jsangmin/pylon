from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
from app.core.database import Base

class JobRun(Base):
    __tablename__ = "tb_job_run"

    job_run_id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("tb_job.job_id"), nullable=False)
    run_status = Column(String, nullable=False)  # RUNNING / SUCCESS / FAIL
    start_time = Column(DateTime(timezone=True), server_default=func.now())
    end_time = Column(DateTime(timezone=True), nullable=True)
    exit_code = Column(Integer, nullable=True)
    error_message = Column(Text, nullable=True)
