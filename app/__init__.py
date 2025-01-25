from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    CORS(app)
    db.init_app(app)
    
    @app.route('/')
    def home():
        return "API Zakupy działa!"

    @app.errorhandler(404)
    def not_found_error(error):
        return "404 - Page Not Found", 404
    
    return app