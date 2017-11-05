import os


class Config:
    """Base configuration."""

    ENV = None

    PATH = os.path.abspath(os.path.dirname(__file__))
    ROOT = os.path.dirname(PATH)
    DEBUG = False
    THREADED = False

class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'

    SECRET_KEY = os.getenv('SECRET_KEY')
    POSTGRES_HOST = os.getenv('POSTGRES_URI')

class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'

    DEBUG = True

    SECRET_KEY = 'dev'
    POSTGRES_DB = 'app_dev'

def get_config(name):
    assert name, "no configuration specified"

    for config in Config.__subclasses__():  # pylint: disable=no-member
        if config.ENV == name:
            return config

    assert False, "no matching configuration"
