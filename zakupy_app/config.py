import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24).hex()
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://marubo:Starszy$pec2023!/@localhost/zakupy_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'mysql+pymysql://marubo:Starszy$pec2023!/@localhost/zakupy_db_test'
    TESTING = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DEBUG = False