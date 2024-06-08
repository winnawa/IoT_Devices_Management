import json
class PushTaskToFeedServiceUtils:
    def __init__(self):
        pass
    @staticmethod     
    def getActionFormat(actionId,taskId):
        if int(actionId) == 1:
            return {
                "Task_id": int(taskId),
                "M1": 10,
                "M2": 10,
                "M3": 10,
                "Area1": True,
                "Area2": False,
                "Area3": True
            }    

class PushTaskToFeedService:
    mqttClient = None
    def __init__(self, mqttClient):
        PushTaskToFeedService.mqttClient = mqttClient
    # @staticmethod
    def execute(self,serializedActionId, serializedTaskId):
        actionId = json.loads(serializedActionId)
        taskId = json.loads(serializedTaskId)

        actionObj = PushTaskToFeedServiceUtils.getActionFormat(actionId,taskId)
        jsonifyDataFormat = json.dumps(actionObj)
        PushTaskToFeedService.mqttClient.publish('task-action',jsonifyDataFormat)