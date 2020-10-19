import flask
from routes.v1 import health, test


def settle(app: flask.Flask):
    # register blueprint
    app.register_blueprint(health)
    app.register_blueprint(test)

    # main route
    @app.route("/")
    def index():
        return "ok"
