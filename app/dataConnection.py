import sqlite3
from pymongo import MongoClient

USER_MONGO = "namkhoapro2804"
PASSWORD_MONGO = "Fw1qQ51eZdTzqlBU"
mongoDbClient = MongoClient("mongodb+srv://namkhoapro2804:{0}@cluster0.lfvuwpu.mongodb.net/".format(PASSWORD_MONGO))


conn = sqlite3.connect('iot_management.db', check_same_thread=False)
curr = conn.cursor()