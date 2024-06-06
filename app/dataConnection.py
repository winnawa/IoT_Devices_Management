from pymongo import MongoClient

USER_MONGO = "khoapham28042002"
PASSWORD_MONGO = "RBGKYYacZOLbsgeN"
mongoDbClient = MongoClient("mongodb+srv://{0}:{1}@cluster0.0dtlntb.mongodb.net/".format(USER_MONGO,PASSWORD_MONGO))


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

class Task(Model):
    description = CharField()
    # "date"== at that time/"interval"== after sometimes/"cron" == time of days
    taskType = CharField()
    createdDate = CharField()
    lastModifiedDate = CharField()

    class Meta:
        database = sqliteDb

sqliteDb.connect()

sqliteDb.create_tables([Device])