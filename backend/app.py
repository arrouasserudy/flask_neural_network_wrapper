from flask import Flask

from backend.utils.logger import configure_logging


def create_app():
    app = Flask(__name__)
    # app.config['SECRET_KEY'] = 'My_Top_Secert_Key'

    configure_logging()
    # Blueprint

    from backend.blueprints.core import bp as bp_core

    bp_core.config(app)

    return app
