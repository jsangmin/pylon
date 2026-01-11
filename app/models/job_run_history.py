from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, BigInteger
from sqlalchemy.sql import func
from app.core.database import Base

class JobRunHistory(Base):
    __tablename__ = "tb_job_run_history"

    job_run_history_id = Column(Integer, primary_key=True, index=True)
    job_run_id = Column(Integer, ForeignKey("tb_job_run.job_run_id"), nullable=False)
    job_id = Column(Integer, ForeignKey("tb_job.job_id"), nullable=False)
    run_status = Column(String, nullable=False)
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=True)
    duration_ms = Column(BigInteger, nullable=True)
    exit_code = Column(Integer, nullable=True)
    error_stacktrace = Column(Text, nullable=True)
