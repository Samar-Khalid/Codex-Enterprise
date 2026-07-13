"""FastAPI application for Codex Enterprise."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..core.config import Settings

settings = Settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Enterprise Application Framework",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "status": "running",
    }


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy"}


@app.get("/api/v1/status")
async def status():
    """System status endpoint."""
    return {
        "api": "operational",
        "database": "connected",
        "cache": "connected",
    }
