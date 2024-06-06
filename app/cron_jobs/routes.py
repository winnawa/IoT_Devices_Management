from datetime import date
import json
from flask import request
from app.cron_jobs import bp
from app.cron_jobs.cronJobUsecases import createBackgroundJob
from app.cron_jobs.dependency_injections.dependency_container import  taskRepository
from app.cron_jobs.usecases.create_task_usecase import CreateTaskUsecase, CreateTaskUsecaseInput
from app.jobSchedulerConnection import scheduler


@bp.route('/', methods=['POST'])
def createTask():
    createTaskObj = {}
    request_data = request.get_json()
    for key in request_data.keys():
        createTaskObj[key] = request_data[key]

    createTaskUsecaseInput = CreateTaskUsecaseInput(createTaskObj)
    createTaskUsecase = CreateTaskUsecase(createTaskUsecaseInput, taskRepository)

    task = createTaskUsecase.execute()
    return json.dumps(
    {
        "message": "create task success",
        "task": task
    }), 200, {'ContentType':'application/json'}
    

    
    createBackgroundJob(task)




@bp.route('/', methods=['GET'])
def index():
    jobs = scheduler.get_jobs()
    print(jobs)
    return 'This is The Cron jobs'

def testCronJob():
    print("this is a cron job in test function")

@bp.route('/', methods=['POST'])
def createCronJob():
    scheduler.add_job(testCronJob, 'date', run_date='2024-04-27 08:30:00')
    return json.dumps({"message": "add cron job success"}), 200, {'ContentType':'application/json'}

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
