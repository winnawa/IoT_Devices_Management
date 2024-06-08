import json
import requests

from app.adafruitConnection import ADAFRUIT_IO_KEY, ADAFRUIT_IO_USERNAME

class GetDeviceDatasServiceUtils:
    def __init__(self):
        pass

class GetDeviceDatasService:
    def __init__(self):
        pass
    def execute(self):
        url = "https://io.adafruit.com/api/v2/{0}/feeds/{1}/data?limit=1".format(ADAFRUIT_IO_USERNAME,"device")
        response = requests.get(url, headers={
            "X-AIO-Key": ADAFRUIT_IO_KEY
        })
        obj = json.loads(response.text)
        deviceDatasObj = json.loads(obj[0]["value"])
        return deviceDatasObj