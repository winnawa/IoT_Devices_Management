from app.cron_jobs.models import CronType

def createBackgroundJob(task):
    if task["cronType"]== CronType.immediate.value:
        runJobImmediate(action)

    return {}
