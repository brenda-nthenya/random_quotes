class Config:
    SECRET_KEY = 'ForWHateverReason'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://bee:QWERTY098@localhost/blogs'
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

class TestConfig():
    pass 

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}