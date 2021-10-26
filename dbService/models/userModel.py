from peewee import IntegerField, CharField

from dbService.models.base import BaseModel


class UserModel(BaseModel):
    t_id = IntegerField()

    name = CharField(max_length=64)

    points = IntegerField(default=0)

