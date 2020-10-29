import os
import pytest
from typing import Generator

from fastapi import FastAPI
from starlette.testclient import TestClient
from tortoise.contrib.fastapi import register_tortoise

from app.app_config import ApplicationSettings, get_application_settings
from app.app_main import create_application


def __get_settings_override__() -> ApplicationSettings:
    """
    Override the application settings and return it
    :return: Object with the application's configuration
    :rtype: ApplicationSettings
    """
    return ApplicationSettings(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))


def __get_test_application__() -> FastAPI:
    """
    Get the API application and change the settings
    :return: Application instance
    :rtype: FastAPI
    """
    app = create_application()
    app.dependency_overrides[get_application_settings] = __get_settings_override__
    return app


@pytest.fixture(scope="module")
def test_app() -> Generator[TestClient, FastAPI, None]:
    """
    Instance the application to test
    :return: test client to make requests
    :rtype: TestClient
    """
    app = __get_test_application__()
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope="module")
def test_app_with_db() -> Generator[TestClient, FastAPI, None]:
    """
    Instance the application to test with database
    :return: test client to make requests
    :rtype: TestClient
    """
    app = __get_test_application__()
    register_tortoise(
        app,
        db_url=os.environ.get("DATABASE_TEST_URL"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
    with TestClient(app) as test_client:
        yield test_client
