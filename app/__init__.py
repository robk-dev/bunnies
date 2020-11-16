from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)

db = MongoEngine()
db.init_app(app)

from app import routes
