from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.job_history import JobHistory as JobHistoryModel
from app.schemas.job_history import JobHistory as JobHistorySchema, JobHistoryCreate, JobHistoryUpdate

router = APIRouter()

@router.post("/", response_model=JobHistorySchema)
def create_job_history(job_history: JobHistoryCreate, db: Session = Depends(get_db)):
    db_job_history = JobHistoryModel(**job_history.model_dump())
    db.add(db_job_history)
    db.commit()
    db.refresh(db_job_history)
    return db_job_history

@router.get("/", response_model=List[JobHistorySchema])
def list_job_histories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    job_histories = db.query(JobHistoryModel).offset(skip).limit(limit).all()
    return job_histories

@router.get("/{job_history_id}", response_model=JobHistorySchema)
def read_job_history(job_history_id: int, db: Session = Depends(get_db)):
    db_job_history = db.query(JobHistoryModel).filter(JobHistoryModel.job_history_id == job_history_id).first()
    if db_job_history is None:
        raise HTTPException(status_code=404, detail="Job history not found")
    return db_job_history

@router.patch("/{job_history_id}", response_model=JobHistorySchema)
def update_job_history(job_history_id: int, job_history_update: JobHistoryUpdate, db: Session = Depends(get_db)):
    db_job_history = db.query(JobHistoryModel).filter(JobHistoryModel.job_history_id == job_history_id).first()
    if db_job_history is None:
        raise HTTPException(status_code=404, detail="Job history not found")
    
    update_data = job_history_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_job_history, key, value)

    db.add(db_job_history)
    db.commit()
    db.refresh(db_job_history)
    return db_job_history

@router.delete("/{job_history_id}")
def delete_job_history(job_history_id: int, db: Session = Depends(get_db)):
    db_job_history = db.query(JobHistoryModel).filter(JobHistoryModel.job_history_id == job_history_id).first()
    if db_job_history is None:
        raise HTTPException(status_code=404, detail="Job history not found")
    
    db.delete(db_job_history)
    db.commit()
    return {"ok": True}
