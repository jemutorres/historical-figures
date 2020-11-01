from pydantic import constr
from typing import Optional

from app.models import Question
from app.schemas.app_schema import AppSchema


class QuestionOutputSchema(AppSchema.model_creator(Question)):
    """
    Schema to return a question
    """
    figure_id: int


class QuestionInputSchema(AppSchema):
    """
    Schema to create/update a question
    """
    question: constr(max_length=300)
    author: Optional[constr(max_length=50)]
