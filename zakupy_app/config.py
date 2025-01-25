import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://marubo:Starszy$pec2023!@localhost/zakupy_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'dev-key'

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://marubo:Starszy$pec2023!@localhost/zakupy_db_test'
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DEBUG = False