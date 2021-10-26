from peewee import IntegerField, CharField, FloatField

from dbService.models.base import BaseModel


class PlayerModel(BaseModel):
    name = CharField(max_length=64)

    nickname = CharField(max_length=64)

    hltv_profile = CharField(max_length=64)

    # team

    maps_played = IntegerField(default=0)

    rating = FloatField(default=0)
