from app.cron_jobs.repositories.task_repository import TaskRepository
from app.cron_jobs.services.mqtt_broker_services.push_task_to_feed_service import PushTaskToFeedService
from app.cron_jobs.services.task_scheduler_services.create_task_schedule_service import CreateTaskScheduleService
from app.cron_jobs.services.task_scheduler_services.delete_task_schedule_service import DeleteTaskScheduleService

class GetTasksUsecaseInput:
    def __init__(self,inputObj):
        self.inputObj = inputObj
class GetTasksUsecase:
    def __init__(self, input : GetTasksUsecaseInput, taskRepository:TaskRepository):
        self.input = input
        self.taskRepository = taskRepository

    def execute(self):
        tasks = self.taskRepository.getTasks()
        return tasks