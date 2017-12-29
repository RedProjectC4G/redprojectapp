import os


class Config:
    """Base configuration."""

    ENV = None

    PATH = os.path.abspath(os.path.dirname(__file__))
    ROOT = os.path.dirname(PATH)
    DEBUG = False
    THREADED = False
    SECRET_KEY = "r0834ht0vgb047gt"

class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'

    MONGO_USER = os.getenv('MONGO_USER')
    MONGO_PW = os.getenv('MONGO_PW')
    MONGO_HOST = os.getenv('MONGO_HOST')
    MONGO_PORT = os.getenv('MONGO_PORT')
    MONGO_DB_NAME = os.getenv('MONGO_DB_NAME')
    MONGO_URI = 'mongodb://{0}:{1}@{2}:{3}/{4}'.format(MONGO_USER, MONGO_PW, MONGO_HOST, MONGO_PORT, MONGO_DB_NAME)
    SECRET_KEY = "r0834ht0vgb047gt"

class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'

    DEBUG = True

    MONGO_HOST = 'localhost'
    MONGO_PORT = '9001'
    MONGO_DB_NAME = 'red_development'
    MONGO_URI = 'mongodb://{}:{}/{}'.format(MONGO_HOST, MONGO_PORT, MONGO_DB_NAME)
    SECRET_KEY = "r0834ht0vgb047gt"

def get_config(name):
    assert name, "no configuration specified"

    for config in Config.__subclasses__():  # pylint: disable=no-member
        if config.ENV == name:
            return config

    assert False, "no matching configuration"
