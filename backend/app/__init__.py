from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import Config, TestConfig, ProductionConfig
from flask_migrate import Migrate
import logging
from logging.handlers import RotatingFileHandler
import os

# Create the SQLAlchemy instance once
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config, test_config=None):
    app = Flask(__name__)
    
    if test_config is None:
        # Konfiguracja aplikacji
        if os.environ.get('FLASK_ENV') == 'testing':
            app.config.from_object(TestConfig)
        elif os.environ.get('FLASK_ENV') == 'production':
            app.config.from_object(ProductionConfig)
        else:
            app.config.from_object(config_class)
    else:
        app.config.from_mapping(test_config)
    
    # Inicjalizacja rozszerzeń
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Import and register blueprints within app context
    with app.app_context():
        from .routes import paragony_bp, produkty_bp
        app.register_blueprint(paragony_bp)
        app.register_blueprint(produkty_bp)
        
        # Create tables if needed
        db.create_all()
    
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

    return app