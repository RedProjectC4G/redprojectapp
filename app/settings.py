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

    POSTGRES_USER = os.getenv('POSTGRES_USER')
    POSTGRES_PW = os.getenv('POSTGRES_PW')
    POSTGRES_HOST = os.getenv('POSTGRES_HOST')
    POSTGRES_PORT = os.getenv('POSTGRES_PORT')
    POSTGRES_DB_NAME = os.getenv('POSTGRES_DB_NAME')
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(POSTGRES_USER, POSTGRES_PW, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB_NAME)

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
