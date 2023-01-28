from flask import Flask
from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    ### BluePrints
    from .main import main_BP
    from .options import options_BP
    from .start import start_BP

    app.register_blueprint(main_BP)
    app.register_blueprint(options_BP)
    app.register_blueprint(start_BP)

    return app


