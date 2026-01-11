from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.job_run_history import JobRunHistory as JobRunHistoryModel
from app.schemas.job_run_history import JobRunHistory as JobRunHistorySchema, JobRunHistoryCreate, JobRunHistoryUpdate

router = APIRouter()

@router.post("/", response_model=JobRunHistorySchema)
def create_job_run_history(job_run_history: JobRunHistoryCreate, db: Session = Depends(get_db)):
    db_job_run_history = JobRunHistoryModel(**job_run_history.model_dump())
    db.add(db_job_run_history)
    db.commit()
    db_job_run_history = db.query(JobRunHistoryModel).filter(JobRunHistoryModel.job_run_history_id == db_job_run_history.job_run_history_id).first()
    return db_job_run_history

@router.get("/", response_model=List[JobRunHistorySchema])
def list_job_run_histories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    job_run_histories = db.query(JobRunHistoryModel).offset(skip).limit(limit).all()
    return job_run_histories

@router.get("/{job_run_history_id}", response_model=JobRunHistorySchema)
def read_job_run_history(job_run_history_id: int, db: Session = Depends(get_db)):
    db_job_run_history = db.query(JobRunHistoryModel).filter(JobRunHistoryModel.job_run_history_id == job_run_history_id).first()
    if db_job_run_history is None:
        raise HTTPException(status_code=404, detail="Job run history not found")
    return db_job_run_history

@router.patch("/{job_run_history_id}", response_model=JobRunHistorySchema)
def update_job_run_history(job_run_history_id: int, job_run_history_update: JobRunHistoryUpdate, db: Session = Depends(get_db)):
    db_job_run_history = db.query(JobRunHistoryModel).filter(JobRunHistoryModel.job_run_history_id == job_run_history_id).first()
    if db_job_run_history is None:
        raise HTTPException(status_code=404, detail="Job run history not found")
    
    update_data = job_run_history_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_job_run_history, key, value)

    db.add(db_job_run_history)
    db.commit()
    db.refresh(db_job_run_history)
    return db_job_run_history

@router.delete("/{job_run_history_id}")
def delete_job_run_history(job_run_history_id: int, db: Session = Depends(get_db)):
    db_job_run_history = db.query(JobRunHistoryModel).filter(JobRunHistoryModel.job_run_history_id == job_run_history_id).first()
    if db_job_run_history is None:
        raise HTTPException(status_code=404, detail="Job run history not found")
    
    db.delete(db_job_run_history)
    db.commit()
    return {"ok": True}
