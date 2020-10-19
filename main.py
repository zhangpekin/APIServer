import routes
from config import conf
from flask import Flask
from utils import logger

app = Flask(__name__)

if __name__ == '__main__':
    logger.info("Server is starting...")
    routes.cross_domain(app)
    routes.settle(app)
    logger.info(app.url_map)
    app.run(
        host='127.0.0.1',
        port=conf.PORT,
        debug=False)
