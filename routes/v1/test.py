from flask import Blueprint
from handles import handleTest

test = Blueprint("test", __name__)


@test.route("/v1/test/data/<path:name>", methods=['GET'])
def test_fetch(name):
    return handleTest(name)
