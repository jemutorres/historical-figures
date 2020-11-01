from typing import Union, List, Type, Dict

from app.models.app_model import AppModel


async def get(
    model: Type[AppModel], identifier: int, filters: Dict = None
) -> Union[Dict, None]:
    """
    Get an object and return it
    :param model: entity model to find
    :param identifier: entity model identifier
    :param filters: filters to find the entity
    :return: Result found if exists
    :rtype: Union[Dict, None]
    """
    filters = filters if filters else {}
    result = await model.filter(id=identifier).filter(**filters).first().values()
    if result:
        return result[0]
    return None


async def get_all(
    model: Type[AppModel], filters: Dict = None
) -> List[Union[Dict, None]]:
    """
    Get a list of objects and return it
    :param model: entity model to find
    :param filters: filters to find the entity
    :return: List of results found if exist
    :rtype: List[Union[Dict, None]]
    """
    filters = filters if filters else {}
    return await model.filter(**filters).all().values()


async def post(model: Type[AppModel], data: Dict) -> Union[AppModel, None]:
    """
    Create an object passed by parameter and return the identifier
    :param model: entity model to create
    :param data: dict with information to create
    :return: Object created
    :rtype: Union[AppModel, None]
    """
    entity = model(**data)
    await entity.save()
    return entity


async def put(model: Type[AppModel], data: Dict, identifier: int) -> Union[Dict, None]:
    """
    Update an object passed by parameter and return it
    :param model: entity model to create
    :param data: dict with information to create
    :param identifier: entity model identifier
    :return: Result updated if exists
    :rtype: Union[Dict, None]
    """
    result = await model.filter(id=identifier).first()
    if not result:
        return None
    result = await model.filter(id=identifier).update(**data)
    if result:
        updated_result = await model.filter(id=identifier).first().values()
        return updated_result[0]
    return None


async def delete(
    model: Type[AppModel], identifier: int, filters: Dict = None
) -> Union[int, None]:
    """
    Delete an object
    :param model: entity model to find
    :param identifier: entity model identifier
    :param filters: filters to find the entity
    :return: identifier of the remove object
    :rtype: Union[int, None]
    """
    filters = filters if filters else {}
    result = await model.filter(id=identifier).filter(**filters).first()
    if not result:
        return None
    await result.delete()
    return identifier
