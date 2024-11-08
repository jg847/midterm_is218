from app.logging_config import setup_logging
from app.config import LOG_LEVEL
from app.calculator import calculator

setup_logging()

if __name__ == "__main__":
    import logging
    logger = logging.getLogger(__name__)
    calculator()
