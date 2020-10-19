from flask import Blueprint

ethereum =  Blueprint("ethereum", __name__)


@ethereum.route("/v1/ethereum/health", methods=['GET'])
def check_ethereum():
    return "ok"

## routes written below