from flask import Blueprint

bp = Blueprint('devices', __name__)

from app.devices import routes