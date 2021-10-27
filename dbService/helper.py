from peewee import InternalError

from dbService.models.base import db
from dbService.models.playerModel import PlayerModel
from dbService.models.events import MapsModel, EventsModel
from dbService.models.userModel import UserModel
from dbService.models.teamModel import TeamModel
from dbService.models.picems import EventsPickEmModel, MapsPickEmModel, TeamsPickEmModel, Top5PickEmModel


def create_tables():
    try:
        db.connect()
        db.create_tables([UserModel, TeamModel, PlayerModel, MapsModel, EventsModel,
                          TeamsPickEmModel, Top5PickEmModel, MapsPickEmModel, EventsPickEmModel, ])
    except InternalError as px:
        print(str(px))

