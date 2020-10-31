from typing import List

from fastapi import APIRouter, Path

from app.api import api
from app.models import Figure
from app.schemas.figure_schema import FigureOutputSchema, FigureInputSchema

router = APIRouter()


@router.get("/{id}/", response_model=FigureOutputSchema, status_code=200)
async def read_figure(id: int = Path(..., gt=0)) -> FigureOutputSchema:
    """
    HTTP GET method to return a figure. Raise HTTPException if not found
    :return: a found figure
    :rtype: FigureOutputSchema
    """
    return await api.read_entity(Figure, id)


@router.get("/", response_model=List[FigureOutputSchema], status_code=200)
async def read_all_figures() -> List[FigureOutputSchema]:
    """
    HTTP GET method to return all figures
    :return: a list of figures
    :rtype: List[FigureOutputSchema]
    """
    return await api.read_all_entities(Figure)


@router.post("/", response_model=FigureOutputSchema, status_code=201)
async def create_figure(payload: FigureInputSchema) -> FigureOutputSchema:
    """
    HTTP POST method to create a figure
    :return: created figure
    :rtype: FigureOutputSchema
    """
    return await api.create_entity(Figure, payload)


@router.put("/{id}/", response_model=FigureOutputSchema, status_code=200)
async def update_figure(payload: FigureInputSchema, id: int = Path(..., gt=0)) -> FigureOutputSchema:
    """
    HTTP PUT method to update a figure
    :return: updated figure
    :rtype: FigureOutputSchema
    """
    return await api.update_entity(Figure, payload, id)


@router.delete("/{id}/", status_code=200)
async def delete_figure(id: int = Path(..., gt=0)) -> FigureOutputSchema:
    """
    HTTP DELETE method to remove a figure
    :return: removed figure
    :rtype: FigureOutputSchema
    """
    return await api.delete_entity(Figure, id)
