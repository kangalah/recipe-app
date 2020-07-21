import os

class Config:
    '''
    General configuration parent class
    '''

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/recipe'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = '\xf3\x00Kd\xbfZ\x9b\xe2W\xe2\xa7\xe0\xe3\xbc\n\xd3j\xd2\xa4Q\xcb\x9f./'
    pass


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/recipe-test'


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/recipe'
    DEBUG = True


    
config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}