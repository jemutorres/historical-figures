from pydantic import constr
from typing import Optional
from datetime import date

from app.models import Figure
from app.schemas.app_schema import AppSchema

# Schema to return a figure
FigureOutputSchema = AppSchema.model_creator(Figure)


class FigureInputSchema(AppSchema):
    """
    Schema to create/update a figure
    """

    name: constr(max_length=50)
    description: str
    birth_date: date
    death_date: Optional[date]
