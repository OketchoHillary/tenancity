import os
from decouple import config as env
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = env('SECRET_KEY')
    BCRYPT_LOG_ROUNDS = env('BCRYPT_LOG_ROUNDS')
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localhost:5432/mypos_db"
    # Static Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    FLASK_APP = 'wsgi.py'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
