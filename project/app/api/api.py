from typing import List, Type, Union, Dict

from fastapi import APIRouter, HTTPException

from app.api import crud
from app.models.app_model import AppModel

router = APIRouter()


async def read_entity(model: Type[AppModel], id: int, filters: Dict = None) -> Union[Dict, None]:
    """
    HTTP GET method to return a entity. Raise HTTPException if not found
    :param model: entity model to find
    :param id: entity model identifier
    :param filters: filters to find the entity
    :return: a found entity
    :rtype: Union[Dict, None]
    """
    entity = await crud.get(model, id, filters)
    if not entity:
        raise HTTPException(status_code=404, detail=f'{model.__name__} not found')

    return entity


async def read_all_entities(model: Type[AppModel], filters: Dict = None) -> List[Union[Dict, None]]:
    """
    HTTP GET method to return all result of a entity
    :param model: entity model to find
    :param filters: filters to find the entity
    :return: a list of result of the passed entity
    :rtype: List[Union[Dict, None]]
    """
    return await crud.get_all(model, filters)


async def create_entity(model: Type[AppModel], payload: Dict) -> AppModel:
    """
    HTTP POST method to create a entity
    :param model: entity model to find
    :param payload: input entity schema
    :return: created entity
    :rtype: AppModel
    """
    entity = await crud.post(model, payload)
    return entity


async def update_entity(model: Type[AppModel], payload: Dict, id: int) -> Union[Dict, None]:
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


async def delete_entity(model: Type[AppModel], id: int, filters: Dict = None) -> None:
    """
    HTTP DELETE method to remove a entity
    :param model: entity model to find
    :param filters: filters to find the entity
    :param id: entity model identifier
    """
    entity = await crud.delete(model, id, filters)
    if not entity:
        raise HTTPException(status_code=404, detail=f'{model.__name__} not found')


async def increase_value_entity(model: Type[AppModel], value: str, id: int) -> None:
    """
    HTTP PUT method to increase the value of a entity
    :param model: entity model to increase value
    :param value: entity model value
    :param id: entity model identifier
    """
    entity = await crud.get(model, id)
    if not entity:
        raise HTTPException(status_code=404, detail=f'{model.__name__} not found')

    await crud.put(model, {value: entity[value] + 1}, id)


async def decrease_value_entity(model: Type[AppModel], value: str, id: int) -> None:
    """
    HTTP PUT method to decrease the value of a entity
    :param model: entity model to increase value
    :param value: entity model value
    :param id: entity model identifier
    """
    entity = await crud.get(model, id)
    if not entity:
        raise HTTPException(status_code=404, detail=f'{model.__name__} not found')
    await crud.put(model, {value: entity[value] - 1}, id)
