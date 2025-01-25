import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://marubo:Starszy$pec2023!/@localhost/zakupy_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://marubo:Starszy$pec2023!/@localhost/zakupy_db_test'
    TESTING = True