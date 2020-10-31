from tortoise import models, fields


class AppModel(models.Model):
    """
    Standard model class of the application
    """
    id = fields.IntField(pk=True)
