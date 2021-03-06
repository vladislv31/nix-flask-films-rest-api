"""Application main module."""

import os

from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
api = Api(
    app,
    doc="/docs"
)

env_config = os.getenv("APP_SETTINGS", "app.config.DevelopmentConfig")
app.config.from_object(env_config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import manage
from app import logging

from app import auth
from app import resources
from app import errors
