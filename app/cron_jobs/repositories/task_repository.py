from peewee import *
from datetime import datetime
from app.dataConnection import Task

class TaskRepositoryUtils:
    @staticmethod
    def mapToTaskDomainModel(tasks : list):
        taskDomainModels = []
        for task in tasks:
            taskDomainModels.append({
                'description': task.description,
                'taskType': task.taskType,
                'createdDate': task.createdDate,
                'id': task.id
            })
        return taskDomainModels
    
class TaskRepository:
    def __init__(self):
        pass

    def createTask(self,createTaskInput):
        try:
            currentUtcTime = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            newTask = Task(description=createTaskInput["description"], taskType = createTaskInput["taskType"], createdDate = currentUtcTime, lastModifiedDate = currentUtcTime)
            if newTask.save() > 0:
                query = (Task
                    .select()
                    .order_by(Task.createdDate.desc())
                    .limit(1))
                
                taskDataModel = None
                for data in query:
                    taskDataModel = data

                if taskDataModel is not None:
                    taskDomainModel = TaskRepositoryUtils.mapToTaskDomainModel([taskDataModel])[0]
                
                    return taskDomainModel
                return None
            return None
        except Exception as error:
            print(error, "inside create task taskRepository")
    
    def getTask(self,taskId):
        try:
            taskDataModel = Task.get_or_none(Task.id == taskId)
            if taskDataModel is not  None:
                taskDomainModel = TaskRepositoryUtils.mapToTaskDomainModel([taskDataModel])[0]
                return taskDomainModel
            return None
        except Exception as error:
            print(error, "inside get task TaskRepository")

    def getTasks(self):
        try:
            query = Task.select()
            taskDataModels=[]
            for task in query:
                taskDataModels.append(task)

            taskDomainModels = TaskRepositoryUtils.mapToTaskDomainModel(taskDataModels)
            return taskDomainModels

        except Exception as error:
            print(error)

    def deleteTask(self,taskId):
        try:
            task = Task.get(Task.id == taskId)
            task.delete_instance()
        except Exception as error:
            print(error)
