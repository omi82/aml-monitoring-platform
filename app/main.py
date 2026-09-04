from fastapi import FastAPI

from app.api.routers.api import api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Enterprise AI-Powered AML Investigation Platform",
    description=(
        "REST APIs for AML Monitoring, "
        "Case Management, Analytics, and AI Investigation."
    ),
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
# Register all API 

@app.get("/", tags=["Root"])
def root():
    """
    Root endpoint.
    """
    return {
        "message": "Welcome to the Enterprise AML API",
        "docs": "/docs",
        "api": "/api/v1",
        "version": "1.0.0",
    }