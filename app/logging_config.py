import logging
from app.config import LOG_LEVEL, LOG_FORMAT

def setup_logging():
    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL.upper(), logging.INFO),
        format=LOG_FORMAT,
        handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler()
        ]
    )
