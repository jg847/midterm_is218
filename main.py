# Importing all necessary files to set up calculator
from app.logging_config import setup_logging
from app.config import LOG_LEVEL
from app.calculator import calculator

# Initializing logging configuration. Ensures all logging messages follow the predefined format
setup_logging()


if __name__ == "__main__": # Script is run directly. 
    import logging # Importing logging module for log messages
    logger = logging.getLogger(__name__) #Get logger instance for the module
    calculator() # Call function to run main application
