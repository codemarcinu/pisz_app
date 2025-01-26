from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate # Zostawiamy import, bo Migrate jest używane w __init__.py
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
cors = CORS()
jwt = JWTManager()
bcrypt = Bcrypt()