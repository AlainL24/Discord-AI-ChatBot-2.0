import logging

logging.basicConfig(
    filename="logs/errors.log",
    level=logging.ERROR
)

def log_error(e):
    logging.error(str(e))