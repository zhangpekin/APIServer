import flask
from flask_cors import CORS

# allow all domain requests
def cross_domain(app :flask.Flask):
    CORS(app, resources=r'/*')