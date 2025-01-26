import os
from zakupy_app import create_app

os.environ['FLASK_ENV'] = 'development'

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        app.run(host='0.0.0.0', port=5001)