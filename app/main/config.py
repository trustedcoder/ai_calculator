"""
Define environment-specific configuration variables
"""

import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Config:
    """Base configuration"""

    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER_UI_DOC_EXPANSION = "list"
    SWAGGER_UI_OPERATION_ID = True


class DevelopmentConfig(Config):
    DEBUG = True
    

class ProductionConfig(Config):
    DEBUG = False


ENV_CONFIG_DICT = dict(dev=DevelopmentConfig, prod=ProductionConfig)


def get_config(config_name):
    """Retrieve environment configuration settings."""
    return ENV_CONFIG_DICT.get(config_name, ProductionConfig)