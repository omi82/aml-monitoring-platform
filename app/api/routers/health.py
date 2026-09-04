from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("")
def health_check():

    return {
        "status": "healthy",
        "service": "Enterprise AML Investigation Platform",
        "version": "1.0.0"
    }