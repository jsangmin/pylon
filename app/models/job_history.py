from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from app.core.database import Base

class JobHistory(Base):
    __tablename__ = "tb_job_history"

    job_history_id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("tb_job.job_id"), nullable=False)
    job_name = Column(String, nullable=False)
    cron_expression = Column(String, nullable=True)
    enabled_yn = Column(Boolean, default=True)
    changed_reason = Column(Text, nullable=True)
