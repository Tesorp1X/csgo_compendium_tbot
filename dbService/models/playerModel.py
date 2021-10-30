from peewee import IntegerField, CharField, FloatField, ForeignKeyField

from dbService.models.base import BaseModel
from dbService.models.teamModel import TeamModel


class PlayerModel(BaseModel):
    name = CharField(max_length=64)

    nickname = CharField(max_length=64)

    hltv_profile = CharField(max_length=64)

    team = ForeignKeyField(TeamModel)

    maps_played = IntegerField(default=0)

    rating = FloatField(default=0)

    class Meta:
        db_table = 'Players'
