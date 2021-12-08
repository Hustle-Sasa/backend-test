import os
import sys
from pathlib import Path  # python3 only


class Config():
    DEBUG = False
    SECRET_KEY = os.getenv("SECRET_KEY", "")
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', '')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI')
    FLASK_ENV = 'testing'

app_configuration = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
}

AppConfig = TestingConfig if 'pytest' in sys.modules else app_configuration.get(os.getenv('FLASK_ENV', 'development'))

