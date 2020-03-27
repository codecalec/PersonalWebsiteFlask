from flask import Flask
from flask_caching import Cache
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

cache = Cache(app)
db = SQLAlchemy(app)

from app import routes, models
