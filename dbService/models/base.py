from peewee import Model, SqliteDatabase


db = SqliteDatabase("csgo_compendium_bot.db")


class BaseModel(Model):
    class Meta:
        database = db
