import logging
import sys

LOG_FORMAT = "[%(levelname)s] %(message)s"


def get_logger():

    logger = logging.getLogger("KreaTrainer")

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)

    formatter = logging.Formatter(LOG_FORMAT)

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger


logger = get_logger()
