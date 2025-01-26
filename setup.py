from setuptools import setup, find_packages

setup(
    name='zakupy_app',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'Flask-Migrate',
        'Flask-CORS',
        'mysqlclient',
    ],
)