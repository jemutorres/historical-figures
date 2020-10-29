import logging
import os
from functools import lru_cache
from pydantic import AnyUrl, BaseSettings

logger = logging.getLogger(__name__)


class ApplicationSettings(BaseSettings):
    """
    Class that define the different settings of the application
    """
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)
    database_url: AnyUrl = os.environ.get("DATABASE_URL")


@lru_cache()  # Cache the settings
def get_application_settings() -> ApplicationSettings:
    """
    Instance the ApplicationSettings and return it
    :return: Object with the application's configuration
    :rtype: ApplicationSettings
    """
    logger.info("Loading configuration settings from the environment...")
    return ApplicationSettings()
