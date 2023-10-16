import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'asgfasgasgfuq12uq88sd8ghshgas00089dsg<jjhsdjhsd/jhsdjsdirttn8934784@?'
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localhost:5432/mypos_db"


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
