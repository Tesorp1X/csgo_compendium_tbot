from peewee import Model, SqliteDatabase


db = SqliteDatabase("../bot_data.db")


class BaseModel(Model):
    class Meta:
        database = db
