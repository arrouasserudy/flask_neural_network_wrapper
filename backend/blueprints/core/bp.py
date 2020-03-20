from flask import Blueprint
bp = Blueprint('core', __name__)


def config(app):
    from backend.blueprints.core import routes
    app.register_blueprint(bp)
