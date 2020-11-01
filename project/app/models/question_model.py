from tortoise import fields

from app.models.app_model import AppModel


class Question(AppModel):
    """
    Class that define a question associated to a character
    """

    question = fields.CharField(max_length=300)
    author = fields.CharField(max_length=50, default="Anonymous", null=True)
    figure = fields.ForeignKeyField("models.Figure", related_name="questions")

    @staticmethod
    def __name__() -> str:
        return "Question"

    def __str__(self) -> str:
        return self.question
