from flask import Flask
from flask_cors import CORS

app = Flask(__name__, static_folder='../static', template_folder='../template')
CORS(app)

def create_app():
    from .route import app_routes
    app.register_blueprint(app_routes)

    return app
