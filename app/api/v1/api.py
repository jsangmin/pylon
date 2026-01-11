from fastapi import APIRouter
from app.api.v1.endpoints import users, notices, roles

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(notices.router, prefix="/notices", tags=["notices"])
api_router.include_router(roles.router, prefix="/roles", tags=["roles"])
