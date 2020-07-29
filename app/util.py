import logging
from logging.config import dictConfig

logger = logging.getLogger(__name__)


def configure_logging():
    """
    Configure the logging facility.

    :return: None
    """

    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "%(asctime)s [%(levelname)s] [%(threadName)s] %(module)s.%(funcName)s - %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "standard",
                "stream": "ext://sys.stdout"
            }
        },
        "root": {
            "level": "DEBUG",
            "handlers": ["console"]
        }
    }

    dictConfig(logging_config)

    logger.info("Logging configured, obviously...")
