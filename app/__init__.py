from flask import Flask
from flask_cors import CORS, cross_origin
from app.socketConnection import socketio
def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    socketio.init_app(app)
    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    from app.devices import bp as devices_bp
    app.register_blueprint(devices_bp, url_prefix='/devices')
    from app.cron_jobs import bp as cron_jobs_bp
    app.register_blueprint(cron_jobs_bp, url_prefix='/cron-jobs')
   
    return app