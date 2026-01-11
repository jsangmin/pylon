from fastapi import APIRouter
from app.api.v1.endpoints import users, notices, roles, jobs, job_runs, job_histories, job_run_histories

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(notices.router, prefix="/notices", tags=["notices"])
api_router.include_router(roles.router, prefix="/roles", tags=["roles"])
api_router.include_router(jobs.router, prefix="/jobs", tags=["jobs"])
api_router.include_router(job_runs.router, prefix="/job_runs", tags=["job_runs"])
api_router.include_router(job_histories.router, prefix="/job_histories", tags=["job_histories"])
api_router.include_router(job_run_histories.router, prefix="/job_run_histories", tags=["job_run_histories"])
