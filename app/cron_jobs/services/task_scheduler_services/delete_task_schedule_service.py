from app.jobSchedulerConnection import scheduler

class DeleteTaskScheduleServiceUtils:
    def __init__(self):
        pass
         
class DeleteTaskScheduleService:
    def __init__(self):
        pass
    def execute(self,taskId):
        scheduler.remove_job(taskId)