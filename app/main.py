from fastapi import FastAPI
from fastapi.openapi.docs import get_redoc_html
from app.core.config import settings
from app.api.v1.api import api_router
from app.core.database import engine, Base
from app.models import user, role, notice

# Create tables (Simplest way for now, better to use Alembic in production)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    redoc_url=None  # Disable default to custom override
)

@app.get("/redoc", include_in_schema=False)
def redoc():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="https://unpkg.com/redoc@2.1.3/bundles/redoc.standalone.js",
    )

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Example"}
