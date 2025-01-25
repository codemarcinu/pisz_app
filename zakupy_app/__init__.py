from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import Config, TestConfig, ProductionConfig
from .extensions import db, migrate
import logging
from logging.handlers import RotatingFileHandler
import os

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    
    # Konfiguracja aplikacji
    if os.environ.get('FLASK_ENV') == 'testing':
        app.config.from_object(TestConfig)
    elif os.environ.get('FLASK_ENV') == 'production':
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(config_class)
    
    # Inicjalizacja rozszerzeń
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Rejestracja blueprintów
    from .routes import main_bp
    app.register_blueprint(main_bp)
    
    # Konfiguracja logowania
    if not app.debug and not app.testing:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/zakupy.log',
                                           maxBytes=10240,
                                           backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Uruchomienie aplikacji Zakupy')

    @app.route('/')
    def home():
        return "API Zakupy działa!"

    @app.errorhandler(404)
    def not_found_error(error):
        return "404 - Page Not Found", 404

    return app