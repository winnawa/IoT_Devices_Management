from pymongo import MongoClient

USER_MONGO = "namkhoapro2804"
PASSWORD_MONGO = "Fw1qQ51eZdTzqlBU"
mongoDbClient = MongoClient("mongodb+srv://namkhoapro2804:{0}@cluster0.lfvuwpu.mongodb.net/".format(PASSWORD_MONGO))


# conn = sqlite3.connect('iot_management.db', check_same_thread=False)
# curr = conn.cursor()
from peewee import *

sqliteDb = SqliteDatabase('iot_management.db')
class Device(Model):
    name = CharField()
    deviceId = CharField()
    deviceType = CharField()
    createdDate = CharField()
    lastModifiedDate = CharField()

    class Meta:
        database = sqliteDb
sqliteDb.connect()

sqliteDb.create_tables([Device])