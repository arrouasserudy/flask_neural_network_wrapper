from backend.blueprints.core.bp import bp
from flask import abort, request
import json

from backend.main import predict_handler
from backend.utils.logger import logger


@bp.route("/health")
def health():
    return "Hello World, I'm healty"


@bp.route("/predict", methods=["POST"])
def predict():
    body = request.get_json()
    url = body.get('url')
    if not url:
        logger.error(f"URL is missing")
        abort(400, {"error": "URL is missing"})

    prediction = predict_handler(url)
    return json.dumps(prediction)
