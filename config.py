import os

basedir = os.path.dirname(os.path.abspath(__file__))

class Config:
    SECRET_KEY = 'supersecretkey'


class DevConfig(Config):
    DEBUG = True

config = {
    'test': DevConfig
}

