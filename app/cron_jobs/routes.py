from app.adafruitConnection import mqttClient
import json
from flask import request
from app.cron_jobs import bp
from app.cron_jobs.dependency_injections.dependency_container import  taskRepository
from app.cron_jobs.services.mqtt_broker_services.push_task_to_feed_service import PushTaskToFeedService
from app.cron_jobs.services.task_scheduler_services.create_task_schedule_service import CreateTaskScheduleService
from app.cron_jobs.services.task_scheduler_services.delete_task_schedule_service import DeleteTaskScheduleService
from app.cron_jobs.usecases.create_task_usecase import CreateTaskUsecase, CreateTaskUsecaseInput
from app.cron_jobs.usecases.delete_task_usecase import DeleteTaskUsecase, DeleteTaskUsecaseInput
from app.cron_jobs.usecases.get_task_usecase import GetTaskUsecase, GetTaskUsecaseInput
from app.cron_jobs.usecases.get_tasks_usecase import GetTasksUsecase, GetTasksUsecaseInput
from app.jobSchedulerConnection import scheduler

@bp.route('/', methods=['POST'])
def createTask():
    createTaskObj = {}
    request_data = request.get_json()
    for key in request_data.keys():
        createTaskObj[key] = request_data[key]

    createTaskUsecaseInput = CreateTaskUsecaseInput(createTaskObj)
    createTaskScheduleService = CreateTaskScheduleService()
    pushTaskToFeedService = PushTaskToFeedService(mqttClient)
    createTaskUsecase = CreateTaskUsecase(createTaskUsecaseInput, taskRepository, createTaskScheduleService, pushTaskToFeedService)

    task = createTaskUsecase.execute()
    return json.dumps(
    {
        "message": "create task success",
        "task": task
    }), 200, {'ContentType':'application/json'}

@bp.route('/<taskId>', methods=['DELETE'])
def deleteTask(taskId):
    deleteTaskUsecaseInput = DeleteTaskUsecaseInput(taskId)
    deleteTaskScheduleService = DeleteTaskScheduleService()
    deleteTaskUsecase = DeleteTaskUsecase(deleteTaskUsecaseInput, taskRepository, deleteTaskScheduleService)

    deleteTaskUsecase.execute()
    return json.dumps(
    {
        "message": "delete task success",
    }), 200, {'ContentType':'application/json'}


@bp.route('/', methods=['GET'])
def index():
    # jobs = scheduler.get_jobs()
    # print(jobs)
    # return 'This is The Cron jobs'
    getTasksUsecaseInput = GetTasksUsecaseInput()
    getTasksUsecase = GetTasksUsecase(getTasksUsecaseInput, taskRepository)

    tasks = getTasksUsecase.execute()
    return json.dumps(
    {
        "message": "get tasks success",
        "tasks": tasks
    }), 200, {'ContentType':'application/json'}

@bp.route('/<taskId>', methods=['GET'])
def getTask(taskId):

    getTaskUsecaseInput = GetTaskUsecaseInput(taskId)
    getTaskUsecase = GetTaskUsecase(getTaskUsecaseInput, taskRepository)

    task = getTaskUsecase.execute()
    return json.dumps(
    {
        "message": "get task success",
        "task": task
    }), 200, {'ContentType':'application/json'}


# def testCronJob():
#     print("this is a cron job in test function")

# @bp.route('/', methods=['POST'])
# def createCronJob():
#     scheduler.add_job(testCronJob, 'date', run_date='2024-04-27 08:30:00')
#     return json.dumps({"message": "add cron job success"}), 200, {'ContentType':'application/json'}

@bp.route('/', methods=['PUT'])
def updateCronJob():
    request_data = request.get_json()
    
    if "isTerminated" in  request_data and request_data["isTerminated"] == True:
        scheduler.shutdown(wait=False)
        return json.dumps({"message": "update cron job success"}), 200, {'ContentType':'application/json'}


    # upateCronJobDto = {}
    # for key in request_data:
    #     createNotificationDto[key] = request_data[key]

    # # add createdTime
    # now = datetime.now()
    # date_time = now.strftime("%Y/%m/%d, %H:%M:%S")
    # print("date and time:",date_time)
    # createNotificationDto["createdTime"] = date_time
