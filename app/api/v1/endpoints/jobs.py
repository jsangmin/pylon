from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.job import Job as JobModel
from app.schemas.job import Job as JobSchema, JobCreate, JobUpdate

router = APIRouter()

@router.post("/", response_model=JobSchema)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    db_job = db.query(JobModel).filter(JobModel.job_name == job.job_name).first()
    if db_job:
        raise HTTPException(status_code=400, detail="Job name already exists")
    
    db_job = JobModel(**job.model_dump())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

@router.get("/", response_model=List[JobSchema])
def list_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    jobs = db.query(JobModel).offset(skip).limit(limit).all()
    return jobs

@router.get("/{job_id}", response_model=JobSchema)
def read_job(job_id: int, db: Session = Depends(get_db)):
    db_job = db.query(JobModel).filter(JobModel.job_id == job_id).first()
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return db_job

@router.patch("/{job_id}", response_model=JobSchema)
def update_job(job_id: int, job_update: JobUpdate, db: Session = Depends(get_db)):
    db_job = db.query(JobModel).filter(JobModel.job_id == job_id).first()
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    
    update_data = job_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_job, key, value)

    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

@router.delete("/{job_id}")
def delete_job(job_id: int, db: Session = Depends(get_db)):
    db_job = db.query(JobModel).filter(JobModel.job_id == job_id).first()
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    
    db.delete(db_job)
    db.commit()
    return {"ok": True}
