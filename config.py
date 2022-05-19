import os

uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

print(uri)
class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY')
    

    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # Mail Configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = uri

class DevConfig(Config):
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://bee:QWERTY098@localhost/blogtest'

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}