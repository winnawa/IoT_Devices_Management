from pytz import utc

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.executors.pool import ThreadPoolExecutor
from app.dataConnection import mongoDbClient

jobstores = {
    'default': MongoDBJobStore("apscheduler","jobs",mongoDbClient)
}
executors = {
    'default': ThreadPoolExecutor(),
}
job_defaults = {
    'coalesce': False,
    'max_instances': 1
}
scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)

# scheduler.start()