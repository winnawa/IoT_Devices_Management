from app.cron_jobs.repositories.task_repository import TaskRepository
from app.cron_jobs.services.mqtt_broker_services.push_task_to_feed_service import PushTaskToFeedService
from app.cron_jobs.services.task_scheduler_services.create_task_schedule_service import CreateTaskScheduleService

class CreateTaskUsecaseInput:
    def __init__(self,inputObj):
        self.inputObj = inputObj
class CreateTaskUsecase:
    def __init__(self, input : CreateTaskUsecaseInput, taskRepository:TaskRepository, createTaskScheduleService: CreateTaskScheduleService, pushTaskToFeedService: PushTaskToFeedService):
        self.input = input
        self.taskRepository = taskRepository
        self.createTaskScheduleService = createTaskScheduleService
        self.pushTaskToFeedService = pushTaskToFeedService

    def execute(self):
        createTaskObj = self.input.inputObj
        task = self.taskRepository.createTask(createTaskObj)
        self.createTaskScheduleService.execute(createTaskObj,str(task["id"]), self.pushTaskToFeedService.execute)

        return task