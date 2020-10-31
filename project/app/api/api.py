from typing import List, Type, Union, Dict

from fastapi import APIRouter, HTTPException

from app.api import crud
from app.models.app_model import AppModel
from app.schemas.app_schema import AppSchema

router = APIRouter()


async def read_entity(model: Type[AppModel], id: int) -> Union[Dict, None]:
    """
    HTTP GET method to return a entity. Raise HTTPException if not found
    :param model: entity model to find
    :param id: entity model identifier
    :return: a found entity
    :rtype: Union[Dict, None]
    """
    entity = await crud.get(model, id)
    if not entity:
        raise HTTPException(status_code=404, detail=f'{model.__name__} not found')

    return entity


async def read_all_entities(model: Type[AppModel]) -> List[Union[Dict, None]]:
    """
    HTTP GET method to return all result of a entity
    :param model: entity model to find
    :return: a list of result of the passed entity
    :rtype: List[Union[Dict, None]]
    """
    return await crud.get_all(model)


async def create_entity(model: Type[AppModel], payload: Type[AppSchema]) -> Type[AppSchema]:
    """
    HTTP POST method to create a entity
    :param model: entity model to find
    :param payload: input entity schema
    :return: created entity
    :rtype: Type[AppSchema]
    """
    entity = await crud.post(model, payload)
    return entity


async def update_entity(model: Type[AppModel], payload: Type[AppSchema], id: int) -> Union[Dict, None]:
    """
    HTTP PUT method to update a entity
    :param model: entity model to find
    :param payload: input entity schema
    :param id: entity model identifier
    :return: updated entity
    :rtype: Union[Dict, None]
    """
    entity = await crud.put(model, payload, id)
    if not entity:
        raise HTTPException(status_code=404, detail=f'{model.__name__} not found')

    return entity


async def delete_entity(model: Type[AppModel], id: int) -> Union[int, None]:
    """
    HTTP DELETE method to remove a entity
    :param model: entity model to find
    :param id: entity model identifier
    :return: removed entity identifier
    :rtype: Union[int, None]
    """
    entity = await crud.delete(model, id)
    if not entity:
        raise HTTPException(status_code=404, detail=f'{model.__name__} not found')

    return entity
