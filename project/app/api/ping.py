from fastapi import APIRouter, Depends

from app.config.config import get_application_settings, ApplicationSettings

router = APIRouter()


@router.get("/")
async def ping(settings: ApplicationSettings = Depends(get_application_settings)):
    return {
        "message": "Welcome to Historical Figures Repository",
        "environment": settings.environment,
        "testing": settings.testing,
    }
