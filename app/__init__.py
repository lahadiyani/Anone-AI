from flask import Flask
from flask_cors import CORS
from .route import app_routes

def create_app():
    app = Flask(__name__, static_folder='../static', template_folder='../template')
    CORS(app)
    app.register_blueprint(app_routes)

    return app
