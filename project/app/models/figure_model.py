from tortoise import fields

from app.models.app_model import AppModel


class Figure(AppModel):
    """
    Class that define a figure of a character
    """
    name = fields.CharField(max_length=50)
    description = fields.TextField()
    birth_date = fields.DateField()
    death_date = fields.DateField(null=True)
    votes = fields.IntField(default=0)

    @staticmethod
    def __name__() -> str:
        return 'Figure'

    def __str__(self) -> str:
        return f'{self.name}, {self.description}'
