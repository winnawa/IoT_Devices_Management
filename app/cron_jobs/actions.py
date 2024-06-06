from app.adafruitConnection import mqttClient

def waterFarm():
    actionObject= {}
    mqttClient.publish('ActionFeed', actionObject)