from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.notice import Notice as NoticeModel
from app.schemas.notice import Notice as NoticeSchema, NoticeCreate, NoticeUpdate

router = APIRouter()

@router.post("/", response_model=NoticeSchema)
def create_notice(notice: NoticeCreate, db: Session = Depends(get_db)):
    db_notice = NoticeModel(**notice.model_dump())
    db.add(db_notice)
    db.commit()
    db.refresh(db_notice)
    return db_notice

@router.get("/", response_model=List[NoticeSchema])
def list_notices(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    notices = db.query(NoticeModel).offset(skip).limit(limit).all()
    return notices

@router.get("/{notice_id}", response_model=NoticeSchema)
def read_notice(notice_id: int, db: Session = Depends(get_db)):
    notice = db.query(NoticeModel).filter(NoticeModel.id == notice_id).first()
    if notice is None:
        raise HTTPException(status_code=404, detail="Notice not found")
    
    # Increase view count
    notice.view_count += 1
    db.commit()
    db.refresh(notice)
    
    return notice

@router.patch("/{notice_id}", response_model=NoticeSchema)
def update_notice(notice_id: int, notice_update: NoticeUpdate, db: Session = Depends(get_db)):
    db_notice = db.query(NoticeModel).filter(NoticeModel.id == notice_id).first()
    if db_notice is None:
        raise HTTPException(status_code=404, detail="Notice not found")
    
    update_data = notice_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_notice, key, value)

    db.add(db_notice)
    db.commit()
    db.refresh(db_notice)
    return db_notice

@router.delete("/{notice_id}")
def delete_notice(notice_id: int, db: Session = Depends(get_db)):
    db_notice = db.query(NoticeModel).filter(NoticeModel.id == notice_id).first()
    if db_notice is None:
        raise HTTPException(status_code=404, detail="Notice not found")
    
    db.delete(db_notice)
    db.commit()
    return {"ok": True}
