from flask import Blueprint

bp = Blueprint('cron-jobs', __name__)

from app.cron_jobs import routes