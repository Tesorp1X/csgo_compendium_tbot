from peewee import IntegerField, CharField

from dbService.models.base import BaseModel


class EventsModel(BaseModel):
    knife_kills = IntegerField(default=0)

    clutches_won_1v4 = IntegerField(default=0)

    clutches_won_1v5 = IntegerField(default=0)

    most_kills_on_single_map = IntegerField(default=0)

    least_deaths_on_single_map = IntegerField(default=0)

    aces = IntegerField(default=0)

    longest_game_rounds = IntegerField(default=0)

    shortest_game_rounds = IntegerField(default=0)

    biggest_rd = IntegerField(default=0)


class MapsModel(BaseModel):
    name = CharField(max_length=16)

    times_played = IntegerField(default=0)
