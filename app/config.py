"""Module with configs for dev and prod."""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    ENV = "production"
    DEBUG = False
    DEVELOPMENT = False
    SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
    RESTFUL_JSON = {"ensure_ascii": False}
    FILMS_PER_PAGE = int(os.getenv("FILMS_PER_PAGE", 10))


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    DEVELOPMENT = True

