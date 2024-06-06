import json
import requests

from app.adafruitConnection import ADAFRUIT_IO_KEY, ADAFRUIT_IO_USERNAME

class GetDeviceDataServiceUtils:
    @staticmethod
    def getFeedKey(deviceId):
        if deviceId == "temp_area1":
            return "temp-area1"
        if deviceId == "temp_area2":
            return "temp-area2"
        if deviceId == "temp_area3":
            return "temp-area3"
        if deviceId == "moisture_area1":
            return "moisture-area1"
        if deviceId == "moisture_area2":
            return "moisture-area2"
        if deviceId == "moisture_area3":
            return "moisture-area3"
        if deviceId == "Water_Pump":
            return "water-pump"
        if deviceId == "Mixer1":
            return "mixer1"
        if deviceId == "Mixer2":
            return "mixer2"
        if deviceId == "Mixer3":
            return "mixer3"
         

class GetDeviceDataService:
    def __init__(self):
        pass
    def execute(self,deviceId):
        deviceFeedKey = GetDeviceDataServiceUtils.getFeedKey(deviceId)
        url = "https://io.adafruit.com/api/v2/{0}/feeds/{1}/data?limit=1".format(ADAFRUIT_IO_USERNAME,deviceFeedKey)
        print(url)
        response = requests.get(url, headers={
            "X-AIO-Key": ADAFRUIT_IO_KEY
        })
        obj = json.loads(response.text)
        deviceData = obj[0]["value"]
        print(deviceData)
        return deviceData