from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel

from typing import Type

from app.models.app_model import AppModel


class AppSchema(BaseModel):
    """
    Standard schema class of the application
    """

    @staticmethod
    def model_creator(model: Type[AppModel]) -> Type[BaseModel]:
        """
        Create a schema from passed model and return it
        :param model: model to create schema
        :return: a schema created from model
        :rtype: Type[BaseModel]
        """
        return pydantic_model_creator(model)


class AppOutputSchema(BaseModel):
    """
    Standard output schema class of the application
    """

    message: str
