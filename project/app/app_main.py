import logging
import os

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.api import ping

logger = logging.getLogger(__name__)


def init_db(application: FastAPI) -> None:
    """
    Init the ORM database
    """
    register_tortoise(
        application,
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["app.models.tortoise_model"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )


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
async def startup_event() -> None:
    """
    Define a handler that will be executed before the app starts up
    """
    logger.info("Starting up...")
    # TODO: Uncomment this line when a tortoise model has been created
    # init_db(app)


@app.on_event("shutdown")
async def shutdown_event() -> None:
    """
    Define a handler that will be executed before the app shutting down
    """
    logger.info("Shutting down...")
