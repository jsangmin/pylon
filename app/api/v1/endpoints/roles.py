from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.role import Role as RoleModel, UserRole as UserRoleModel
from app.schemas.role import Role as RoleSchema, RoleCreate, UserRoleCreate

router = APIRouter()

@router.post("/", response_model=RoleSchema)
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    db_role = db.query(RoleModel).filter(RoleModel.name == role.name).first()
    if db_role:
        raise HTTPException(status_code=400, detail="Role already exists")
    
    db_role = RoleModel(name=role.name, description=role.description)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

@router.get("/", response_model=List[RoleSchema])
def list_roles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    roles = db.query(RoleModel).offset(skip).limit(limit).all()
    return roles

@router.post("/assign", response_model=UserRoleCreate)
def assign_role_to_user(assignment: UserRoleCreate, db: Session = Depends(get_db)):
    # Check if assignment already exists
    existing = db.query(UserRoleModel).filter(
        UserRoleModel.user_id == assignment.user_id,
        UserRoleModel.role_id == assignment.role_id
    ).first()
    
    if existing:
        return assignment

    db_user_role = UserRoleModel(user_id=assignment.user_id, role_id=assignment.role_id)
    db.add(db_user_role)
    db.commit()
    return assignment
