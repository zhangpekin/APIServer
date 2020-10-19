from flask import Blueprint

health = Blueprint("health", __name__)


@health.route("/v1/health", methods=['GET'])
def health_check():
    return "ok"
