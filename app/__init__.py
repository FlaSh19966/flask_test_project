from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_restful import Api

from celery import Celery
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'login'

celery = Celery(__name__, broker=Config.CELERY_BROKER_URL, include=['app', 'app.tasks', 'tasks'])

app = Flask(__name__)
api = Api(app)

app.config.from_object(Config)

db.init_app(app)
db.create_all()

login_manager.init_app(app)
celery.conf.update(app.config)


from app import routes
app.register_blueprint(routes.master_blueprint)


