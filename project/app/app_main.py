import logging
import os

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.api import figure_router, ping_router, question_router

logger = logging.getLogger(__name__)


def init_db(application: FastAPI) -> None:
    """
    Init the ORM database
    """
    register_tortoise(
        application,
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["app.models"]},
        generate_schemas=False,
        add_exception_handlers=False,
    )


def create_application() -> FastAPI:
    """
    Create the application and return it
    :return: Application instance
    :rtype: FastAPI
    """
    application = FastAPI(
        title="Historical Figures Repository",
        description="Interactive repository for History students",
        version="1.0",
    )
    application.include_router(ping_router.router)
    application.include_router(figure_router.router, prefix="/figures", tags=["Figure"])
    application.include_router(
        question_router.router,
        prefix="/figures/{figure_id}/questions",
        tags=["Question"],
    )
    return application


app = create_application()


@app.on_event("startup")
async def startup_event() -> None:
    """
    Define a handler that will be executed before the app starts up
    """
    logger.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event() -> None:
    """
    Define a handler that will be executed before the app shutting down
    """
    logger.info("Shutting down...")
