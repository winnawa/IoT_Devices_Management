from datetime import date
import json
from flask import request
from app.cron_jobs import bp
from app.jobSchedulerConnection import scheduler


@bp.route('/', methods=['GET'])
def index():
    jobs = scheduler.get_jobs()
    print(jobs)
    return 'This is The Cron jobs'

def testCronJob():
    print("this is a cron job in test function")

@bp.route('/', methods=['POST'])
def createCronJob():
    scheduler.add_job(testCronJob, 'date', run_date='2024-04-26 18:03:00')
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
