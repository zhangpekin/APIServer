import os
import sys
import logging
from logging.config import dictConfig

# logger util, level is 'INFO'

LOGGING_CONFIG = dict(
    version=1,
    loggers={
        "app": {
            "level": "INFO",
            "handlers": ["console"]
        },
        "root": {
            "level": "INFO",
            "handlers": []
        }
    },
    handlers={
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "generic",
            "stream": sys.stdout
        },
        "access_console": {
            "class": "logging.StreamHandler",
            "formatter": "access",
            "stream": sys.stdout
        },
    },
    formatters={
        "generic": {
            "format":
            "%(asctime)s - (%(name)s) [%(levelname)s] %(filename)s:%(lineno)d | %(message)s",
            "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
            "class": "logging.Formatter"
        },
        "access": {
            "format": "%(asctime)s - (%(name)s)[%(levelname)s][%(host)s]: " +
            "%(request)s %(message)s %(status)d %(byte)d",
            "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
            "class": "logging.Formatter"
        },
    })

dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('app')
