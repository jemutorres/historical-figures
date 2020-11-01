from typing import List

from fastapi import APIRouter, Path

from app.api import api
from app.models import Question
from app.schemas.app_schema import AppOutputSchema
from app.schemas.question_schema import QuestionOutputSchema, QuestionInputSchema

router = APIRouter()


@router.get("/{id}/", response_model=QuestionOutputSchema, status_code=200)
async def read_question(figure_id: int = Path(..., gt=0), id: int = Path(..., gt=0)) -> QuestionOutputSchema:
    """
    HTTP GET method to return a question. Raise HTTPException if not found
    """
    return await api.read_entity(Question, id, {'figure_id': figure_id})


@router.get("/", response_model=List[QuestionOutputSchema], status_code=200)
async def read_all_questions(figure_id: int = Path(..., gt=0)) -> List[QuestionOutputSchema]:
    """
    HTTP GET method to return all questions
    """
    return await api.read_all_entities(Question, {'figure_id': figure_id})


@router.post("/", response_model=QuestionOutputSchema, status_code=201)
async def create_question(payload: QuestionInputSchema, figure_id: int = Path(..., gt=0)) -> QuestionOutputSchema:
    """
    HTTP POST method to create a question
    """
    return await api.create_entity(Question, {**payload.__dict__, **{'figure_id': figure_id}})


@router.put("/{id}/", response_model=QuestionOutputSchema, status_code=200)
async def update_question(payload: QuestionInputSchema, figure_id: int = Path(..., gt=0),
                          id: int = Path(..., gt=0)) -> QuestionOutputSchema:
    """
    HTTP PUT method to update a question
    """
    return await api.update_entity(Question, {**payload.__dict__, **{'figure_id': figure_id}}, id)


@router.delete("/{id}/", response_model=AppOutputSchema, status_code=200)
async def delete_question(figure_id: int = Path(..., gt=0), id: int = Path(..., gt=0)) -> AppOutputSchema:
    """
    HTTP DELETE method to remove a question
    """
    await api.delete_entity(Question, id, {'figure_id': figure_id})
    return AppOutputSchema(message='Question deleted successfully')