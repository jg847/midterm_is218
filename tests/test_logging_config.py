import logging
import pytest
from app.logging_config import setup_logging
from app.config import LOG_LEVEL

@pytest.fixture
def reset_logging():
    """Fixture to reset logging configuration after each test."""
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.root.setLevel(logging.NOTSET)

def test_setup_logging(reset_logging, caplog):
    """Test that logging is configured correctly."""
    setup_logging()
    logger = logging.getLogger("test_logger")
    
    # Log at all levels
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    
    # Check the log output
    assert caplog.records[0].levelname == "INFO"
    assert caplog.records[0].message == "This is an info message."
    assert caplog.records[1].levelname == "WARNING"
    assert caplog.records[1].message == "This is a warning message."
    assert caplog.records[2].levelname == "ERROR"
    assert caplog.records[2].message == "This is an error message."
   

def test_log_level_from_config(reset_logging, caplog):
    """Test that the LOG_LEVEL from the configuration is applied."""
    setup_logging()
    logger = logging.getLogger("test_logger")
    
    logger.info("This debug message should appear at default INFO level.")
    assert len(caplog.records) == 1  # No log messages should appear at DEBUG level