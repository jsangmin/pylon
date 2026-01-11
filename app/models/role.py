from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class Role(Base):
    __tablename__ = "tb_role"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=True)

class UserRole(Base):
    __tablename__ = "tb_user_role"

    user_id = Column(Integer, ForeignKey("tb_user.id"), primary_key=True)
    role_id = Column(Integer, ForeignKey("tb_role.id"), primary_key=True)
    granted_at = Column(DateTime(timezone=True), server_default=func.now())
