from flask import jsonify
from models import Test

def handleTest(name):
    test = Test(2020,name)
    test.render()

    return jsonify(test.format())