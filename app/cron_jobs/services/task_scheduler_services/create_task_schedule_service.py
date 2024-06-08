import json
import requests
from app.jobSchedulerConnection import scheduler

class CreateTaskScheduleServiceUtils:
    def __init__(self):
        pass
         
class CreateTaskScheduleService:
    def __init__(self):
        pass
    def execute(self,taskInputObj,taskId,action):

        serializedTaskActionId = json.dumps(taskInputObj["taskActionId"])       
        serialiseTaskId = json.dumps(taskId)

        if taskInputObj["taskType"] == "immediate":
            scheduler.add_job(action, args=[serializedTaskActionId,serialiseTaskId], trigger= None, id= taskId)
        if taskInputObj["taskType"] == "date":
            # taskInputObj['runDate'] = '2024-04-27 08:30:00'
            scheduler.add_job(action, args=[serializedTaskActionId,serialiseTaskId], trigger="date", run_date=taskInputObj['runDate'], id= taskId)
        if taskInputObj["taskType"] == "interval":
            scheduler.add_job(action, args=[serializedTaskActionId,serialiseTaskId], trigger="interval", minutes = int(taskInputObj["interval"]) , id= taskId)        
        if taskInputObj["taskType"] == "cron":
            scheduler.add_job(action, args=[serializedTaskActionId,serialiseTaskId], trigger="cron", day_of_week='mon-fri', hour= int(taskInputObj["hour"]), minute=int(taskInputObj["minute"]), id= taskId)
