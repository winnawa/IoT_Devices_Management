from app.cron_jobs.repositories.task_repository import TaskRepository
from app.cron_jobs.services.mqtt_broker_services.push_task_to_feed_service import PushTaskToFeedService
from app.cron_jobs.services.task_scheduler_services.create_task_schedule_service import CreateTaskScheduleService
from app.cron_jobs.services.task_scheduler_services.delete_task_schedule_service import DeleteTaskScheduleService

class DeleteTaskUsecaseInput:
    def __init__(self,taskId):
        self.taskId = taskId
class DeleteTaskUsecase:
    def __init__(self, input : DeleteTaskUsecaseInput, taskRepository:TaskRepository, deleteTaskScheduleService: DeleteTaskScheduleService):
        self.input = input
        self.taskRepository = taskRepository
        self.deleteTaskScheduleService = deleteTaskScheduleService

    def execute(self):
        taskId = self.input.taskId
        self.taskRepository.deleteTask(taskId)

        self.deleteTaskScheduleService.execute(taskId)