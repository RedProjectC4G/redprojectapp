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

    MONGODB_USER = os.getenv('MONGODB_USER')
    MONGODB_PW = os.getenv('MONGODB_PW')
    MONGODB_HOST = os.getenv('MONGODB_HOST')
    MONGODB_PORT = os.getenv('MONGODB_PORT')
    MONGODB_DB = os.getenv('MONGODB_DB')
    SECRET_KEY = "r0834ht0vgb047gt"

class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'

    DEBUG = True
    MONGODB_HOST = os.getenv('MONGODB_HOST', default='localhost')
    MONGODB_DB = os.getenv('MONGODB_DB', default='red_development')
    SECRET_KEY = "r0834ht0vgb047gt"

def get_config(name):
    assert name, "no configuration specified"

    for config in Config.__subclasses__():  # pylint: disable=no-member
        if config.ENV == name:
            return config

    assert False, "no matching configuration"
