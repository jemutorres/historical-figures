from typing import List

from fastapi import APIRouter, Path

from app.api import api
from app.models import Figure
from app.schemas.app_schema import AppOutputSchema
from app.schemas.figure_schema import FigureOutputSchema, FigureInputSchema

router = APIRouter()


@router.get("/{id}/", response_model=FigureOutputSchema, status_code=200)
async def read_figure(id: int = Path(..., gt=0)) -> FigureOutputSchema:
    """
    HTTP GET method to return a figure. Raise HTTPException if not found
    """
    return await api.read_entity(Figure, id)


@router.get("/", response_model=List[FigureOutputSchema], status_code=200)
async def read_all_figures() -> List[FigureOutputSchema]:
    """
    HTTP GET method to return all figures
    """
    return await api.read_all_entities(Figure)


@router.post("/", response_model=FigureOutputSchema, status_code=201)
async def create_figure(payload: FigureInputSchema) -> FigureOutputSchema:
    """
    HTTP POST method to create a figure
    """
    return await api.create_entity(Figure, payload.__dict__)


@router.put("/{id}/", response_model=FigureOutputSchema, status_code=200)
async def update_figure(
    payload: FigureInputSchema, id: int = Path(..., gt=0)
) -> FigureOutputSchema:
    """
    HTTP PUT method to update a figure
    """
    return await api.update_entity(Figure, payload.__dict__, id)


@router.delete("/{id}/", response_model=AppOutputSchema, status_code=200)
async def delete_figure(id: int = Path(..., gt=0)) -> AppOutputSchema:
    """
    HTTP DELETE method to remove a figure
    """
    await api.delete_entity(Figure, id)
    return AppOutputSchema(message="Figure deleted successfully")


@router.post("/{id}/votes/up/", response_model=AppOutputSchema, status_code=200)
async def vote_up_figure(id: int = Path(..., gt=0)) -> FigureOutputSchema:
    """
    HTTP POST method to vote up a figure
    """
    await api.increase_value_entity(Figure, "votes", id)
    return AppOutputSchema(message="Figure voted down successfully")


@router.post("/{id}/votes/down/", response_model=AppOutputSchema, status_code=200)
async def vote_down_figure(id: int = Path(..., gt=0)) -> AppOutputSchema:
    """
    HTTP POST method to vote down a figure
    """
    await api.decrease_value_entity(Figure, "votes", id)
    return AppOutputSchema(message="Figure voted down successfully")
