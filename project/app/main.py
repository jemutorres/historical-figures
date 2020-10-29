import logging
from fastapi import FastAPI

from app.api import ping

logger = logging.getLogger(__name__)


def create_application() -> FastAPI:
    """
    Create the application and return it
    :return: Application instance
    :rtype: FastAPI
    """
    application = FastAPI(title="Historical Figures Repository",
                          description="Interactive repository for History students",
                          version="1.0")
    application.include_router(ping.router)
    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    """
    Define a handler that will be executed before the app starts up
    """
    logger.info("Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    """
    Define a handler that will be executed before the app shutting down
    """
    logger.info("Shutting down...")
