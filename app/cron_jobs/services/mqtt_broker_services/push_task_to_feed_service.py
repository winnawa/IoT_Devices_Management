import json
import requests

from app.adafruitConnection import ADAFRUIT_IO_KEY, ADAFRUIT_IO_USERNAME
from app.adafruitConnection import mqttClient
class PushTaskToFeedServiceUtils:
    def __init__(self):
        pass     

class PushTaskToFeedService:
    def __init__(self):
        pass
    @staticmethod
    def execute():
        mqttClient.publish('DemoFeed',{})