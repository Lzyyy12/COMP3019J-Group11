import os
import logging
from logging.handlers import RotatingFileHandler


def get_cwd():
    return os.path.dirname(os.path.abspath(__file__))


def log_config():
    # log level
    logging.basicConfig(level=logging.INFO)

    # log outpath
    log_path = os.path.join(get_cwd(), 'recipe_web.log')
    # loghandler size and amount
    file_log_handler = RotatingFileHandler(
        log_path, encoding='UTF-8', maxBytes=1024*1024*100, backupCount=100)
    # log format
    formatter = logging.Formatter(
        "%(levelname)s %(asctime)s [%(filename)s]: %(lineno)s - %(funcName)s - %(message)s")
    file_log_handler.setFormatter(formatter)

    logging.getLogger().addHandler(file_log_handler)