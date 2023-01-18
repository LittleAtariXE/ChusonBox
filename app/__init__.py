from flask import Flask
from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    ### BluePrints
    from .main import main_BP

    app.register_blueprint(main_BP)

    return app


