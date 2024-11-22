import logging
from logging.handlers import RotatingFileHandler

def set_logging(log_file="bot.log"):
    log_format = "%(levelname)s - %(asctime)s - %(name)s - %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        datefmt=date_format,
        handlers=[
            logging.StreamHandler(),
            RotatingFileHandler(
                log_file, maxBytes = 5 * 1024 * 1024, backupCount=2
            ),
        ],
    )