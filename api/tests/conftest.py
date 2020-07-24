import os
import pathlib
import sys
import pytest
import dotenv
import logging.config

dotenv.load_dotenv(dotenv.find_dotenv())
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "[%(asctime)s] [%(level"
                      "name)s] [%(name)s] "
            "[%(module)s:%(lineno)d] %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        }
    },
    "loggers": {"flask_prometheus_grafana_example": {"level": os.getenv("LOG_LEVEL", "INFO"), "handlers": ["console"],}},
}
logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger("flask_prometheus_grafana_example")
logger.debug("Initialized logger")
