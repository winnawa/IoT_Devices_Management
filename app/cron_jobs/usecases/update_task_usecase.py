from app.cron_jobs.repositories.task_repository import TaskRepository

class UpdateTaskUsecaseInput:
    def __init__(self,inputObj,taskId):
        self.inputObj = inputObj
        self.taskId = taskId
class UpdateTaskUsecase:
    def __init__(self, input : UpdateTaskUsecaseInput, taskRepository:TaskRepository):
        self.input = input
        self.taskRepository = taskRepository

    def execute(self):
        updateTaskObj = self.input.inputObj
        taskId = self.input.taskId
        updatedTask = self.taskRepository.updateTask(taskId,updateTaskObj)
        return updatedTask