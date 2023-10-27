import os
from decouple import config as env
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = env('SECRET_KEY')
    BCRYPT_LOG_ROUNDS = env('BCRYPT_LOG_ROUNDS')
    SQLALCHEMY_DATABASE_URI = env('DATABASE_URI')
    # Static Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    FLASK_APP = 'wsgi.py'


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

    # mail setup
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 587
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_DEBUG = DEBUG
    MAIL_USERNAME = env('MAIL_USERNAME')
    MAIL_PASSWORD = env('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = 'info@denfainvt.com'
    MAIL_MAX_EMAILS = None
    MAIL_SUPPRESS_SEND = TestingConfig.TESTING
    MAIL_ASCII_ATTACHMENTS = False

