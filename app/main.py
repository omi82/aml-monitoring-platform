from fastapi import FastAPI

from app.api.routers.api import api_router
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers.ai_chat import router as ai_chat_router

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
app.include_router(
    ai_chat_router,
    prefix="/api/v1",
)
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