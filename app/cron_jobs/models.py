from enum import Enum

class CronType(Enum):
    immediate = '0'
    date = '1'
    interval = '2'
    cron = '3'

class TaskAction(Enum):
    wateringFarm = '0'
    
