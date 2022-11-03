from .config import get_config
from flask import Flask
from flask_cors import CORS


cors = CORS()


def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(get_config(config_name))

    # register blueprints
    from app import core_blueprint

    app.register_blueprint(core_blueprint)

    # add extensions
    extensions(app)


    return app


def extensions(app):
    cors.init_app(app)
    return None