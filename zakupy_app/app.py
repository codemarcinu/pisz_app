from flask import Flask
import os
from config import Config
from config import TestConfig
from extensions import db, migrate

app = Flask(__name__)
if os.environ.get('FLASK_ENV') == 'testing':
    app.config.from_object(TestConfig)
else:
    app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

@app.route('/')
def home():
    return "API Zakupy działa!"

if __name__ == '__main__':
    app.run(debug=True, port=5001)