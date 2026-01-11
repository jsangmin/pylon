from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.job_run import JobRun as JobRunModel
from app.schemas.job_run import JobRun as JobRunSchema, JobRunCreate, JobRunUpdate

router = APIRouter()

@router.post("/", response_model=JobRunSchema)
def create_job_run(job_run: JobRunCreate, db: Session = Depends(get_db)):
    db_job_run = JobRunModel(**job_run.model_dump())
    db.add(db_job_run)
    db.commit()
    db.refresh(db_job_run)
    return db_job_run

@router.get("/", response_model=List[JobRunSchema])
def list_job_runs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    job_runs = db.query(JobRunModel).offset(skip).limit(limit).all()
    return job_runs

@router.get("/{job_run_id}", response_model=JobRunSchema)
def read_job_run(job_run_id: int, db: Session = Depends(get_db)):
    db_job_run = db.query(JobRunModel).filter(JobRunModel.job_run_id == job_run_id).first()
    if db_job_run is None:
        raise HTTPException(status_code=404, detail="Job run not found")
    return db_job_run

@router.patch("/{job_run_id}", response_model=JobRunSchema)
def update_job_run(job_run_id: int, job_run_update: JobRunUpdate, db: Session = Depends(get_db)):
    db_job_run = db.query(JobRunModel).filter(JobRunModel.job_run_id == job_run_id).first()
    if db_job_run is None:
        raise HTTPException(status_code=404, detail="Job run not found")
    
    update_data = job_run_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_job_run, key, value)

    db.add(db_job_run)
    db.commit()
    db.refresh(db_job_run)
    return db_job_run

@router.delete("/{job_run_id}")
def delete_job_run(job_run_id: int, db: Session = Depends(get_db)):
    db_job_run = db.query(JobRunModel).filter(JobRunModel.job_run_id == job_run_id).first()
    if db_job_run is None:
        raise HTTPException(status_code=404, detail="Job run not found")
    
    db.delete(db_job_run)
    db.commit()
    return {"ok": True}
