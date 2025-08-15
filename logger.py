
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def get_logger(name: str | None = None) -> logging.Logger:
    return logging.getLogger(name if name else __name__)

