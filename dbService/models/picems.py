from peewee import IntegerField, CharField, ForeignKeyField, BooleanField

from dbService.models.base import BaseModel
from dbService.models.userModel import UserModel
from dbService.models.playerModel import PlayerModel
from dbService.models.teamModel import TeamModel
from dbService.models.events import MapsModel


class BasePickEmModel(BaseModel):
    user = ForeignKeyField(UserModel)


class TeamsPickEmModel(BasePickEmModel):
    team1 = ForeignKeyField(TeamModel)

    team2 = ForeignKeyField(TeamModel)

    team3 = ForeignKeyField(TeamModel)

    team4 = ForeignKeyField(TeamModel)

    team5 = ForeignKeyField(TeamModel)

    team6 = ForeignKeyField(TeamModel)

    team7 = ForeignKeyField(TeamModel)

    team8 = ForeignKeyField(TeamModel)

    team9 = ForeignKeyField(TeamModel)


class Top5PickEmModel(BasePickEmModel):
    player1 = ForeignKeyField(PlayerModel)

    player2 = ForeignKeyField(PlayerModel)

    player3 = ForeignKeyField(PlayerModel)

    player4 = ForeignKeyField(PlayerModel)

    player5 = ForeignKeyField(PlayerModel)


class MapsPickEmModel(BasePickEmModel):
    most_popular_map = ForeignKeyField(MapsModel)

    less_popular_map = ForeignKeyField(MapsModel)


class EventsPickEmModel(BasePickEmModel):
    winners = ForeignKeyField(TeamModel)

    knife_kills = CharField(max_length=16, choices=(('0', '0 kills'),
                                                    ('1-5', '1 - 5 kills'),
                                                    ('6-10', '6 - 10 kills'),
                                                    ('11', 'More than 10 kills')
                                                    ))

    clutches_won_1v4 = BooleanField(default=False)

    clutches_won_1v5 = BooleanField(default=False)

    most_kills_on_single_map = CharField(max_length=16, choices=(('20-24', '20 - 24 kills'),
                                                                 ('25-30', '25 - 30 kills'),
                                                                 ('31-35', '31 - 35 kills'),
                                                                 ('36', 'More than 36 kills')))

    least_deaths_on_single_map = CharField(max_length=16, choices=(('0', '0 deaths'),
                                                                   ('1-5', '1 - 5 deaths'),
                                                                   ('6-10', '6 - 10 deaths'),
                                                                   ('11-15', '11 - 15 deaths')))

    aces = CharField(max_length=16, choices=(('1', '1'),
                                             ('2', '2'),
                                             ('3', '3'),
                                             ('4', '4'),
                                             ('5', '5'),
                                             ('6', 'More than 5 aces')))

    longest_game_rounds = CharField(max_length=16, choices=(('30-35', '30 - 35 rounds'),
                                                            ('36-40', '36 - 40 rounds'),
                                                            ('41-45', '41 - 45 rounds'),
                                                            ('46', 'More than 45 rounds')))

    shortest_game_rounds = CharField(max_length=16, choices=(('16', '16 rounds'),
                                                             ('17-19', '17 - 19 rounds'),
                                                             ('20-22', '20 - 22 rounds'),
                                                             ('23-25', '23 - 25 rounds'),
                                                             ('26', 'More than 25 rounds')))

    biggest_rd = CharField(max_length=16, choices=(('1-12', '1-12'),
                                                   ('13-25', '13-25'),
                                                   ('26-38', '26-38'),
                                                   ('39', 'More than 38')))
