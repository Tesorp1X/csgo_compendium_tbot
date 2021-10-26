from peewee import IntegerField, CharField

from dbService.models.base import BaseModel


class TeamModel(BaseModel):
    name = CharField(max_length=64)

    wins = IntegerField(default=0)

    losses = IntegerField(default=0)

    # best_player

    maps_played = IntegerField(default=0)

    round_diff = IntegerField(default=0)

    q_status = CharField(max_length=4, choices=(('q', 'Qualified'),
                                                ('n', 'Not Qualified'),
                                                ('tbd', 'TBD')))
