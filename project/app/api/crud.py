from typing import Union, List, Type, Dict
from app.models.app_model import AppModel
from app.schemas.app_schema import AppSchema


async def get(model: Type[AppModel], identifier: int) -> Union[Dict, None]:
    """
    Get an object and return it
    :param model: entity model to find
    :param identifier: entity model identifier
    :return: Result found if exists
    :rtype: Union[Dict, None]
    """
    result = await model.filter(id=identifier).first().values()
    if result:
        return result[0]
    return None


async def get_all(model: Type[AppModel]) -> List[Union[Dict, None]]:
    """
    Get a list of objects and return it
    :param model: entity model to find
    :return: List of results found if exist
    :rtype: List[Union[Dict, None]]
    """
    result = await model.all().values()
    return result


async def post(model: Type[AppModel], schema: Type[AppSchema]) -> Union[Dict, None]:
    """
    Create an object passed by parameter and return the identifier
    :param model: entity model to create
    :param schema: schema with information to create
    :return: Object created
    :rtype: Union[Dict, None]
    """
    entity = model(**schema.__dict__)
    await entity.save()
    return entity


async def put(model: Type[AppModel], schema: Type[AppSchema], identifier: int) -> Union[Dict, None]:
    """
    Update an object passed by parameter and return it
    :param model: entity model to create
    :param schema: schema with information to create
    :param identifier: entity model identifier
    :return: Result updated if exists
    :rtype: Union[Dict, None]
    """
    result = await model.filter(id=identifier).first()
    if not result:
        raise Exception(f'{model.__class__.__name__} not found')
    result = await model.filter(id=identifier).update(**schema.__dict__)
    if result:
        updated_result = await model.filter(id=identifier).first().values()
        return updated_result[0]
    return None


async def delete(model: Type[AppModel], identifier: int) -> Union[int, None]:
    """
    Delete an object
    :param model: entity model to find
    :param identifier: entity model identifier
    :return: identifier of the remove object
    :rtype: Union[int, None]
    """
    result = await model.filter(id=identifier).first()
    if not result:
        return None
    await result.delete()
    return {'id': identifier}
